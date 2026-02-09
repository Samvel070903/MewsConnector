"""Couche de transport HTTP bas niveau utilisant *httpx*."""

from __future__ import annotations

import logging
import time
from typing import Any

import httpx

from mews.errors import (
    MewsAPIError,
    MewsAuthError,
    MewsNotFoundError,
    MewsRateLimitError,
    MewsValidationError,
)

logger = logging.getLogger("mews.transport")

# Codes d'erreur Mews correspondant à des exceptions spécifiques
_AUTH_CODES = {"InvalidAccessToken", "InvalidClientToken", "AccessTokenExpired"}
_VALIDATION_CODES = {"InvalidRequest", "ValidationFailed"}


class Transport:
    """Enveloppe légère autour de :mod:`httpx` avec réessais et gestion d'erreurs.

    Cette classe n'est **pas** destinée à être utilisée directement — elle
    est consommée par :class:`mews.client.MewsClient`.
    """

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self._base_url = base_url
        self._timeout = timeout
        self._max_retries = max_retries
        self._session = httpx.Client(
            base_url=base_url,
            timeout=httpx.Timeout(timeout),
            headers={"Content-Type": "application/json"},
        )

    # ------------------------------------------------------------------ #
    # Public
    # ------------------------------------------------------------------ #

    def request(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Envoie une requête POST vers *endpoint* avec *payload*.

        L'API Mews Connector utilise ``POST`` pour toutes les opérations.

        Returns:
            Réponse JSON parsée sous forme de ``dict``.

        Raises:
            MewsAuthError: en cas de problème d'authentification/token.
            MewsRateLimitError: en cas de HTTP 429.
            MewsValidationError: en cas d'erreur de validation du payload.
            MewsNotFoundError: en cas de HTTP 404.
            MewsAPIError: pour toute autre erreur API.
        """
        url = f"/api/connector/v1/{endpoint.lstrip('/')}"
        last_exc: Exception | None = None

        for attempt in range(1, self._max_retries + 1):
            try:
                logger.debug("POST %s (tentative %d/%d)", url, attempt, self._max_retries)
                resp = self._session.post(url, json=payload)
                return self._handle_response(resp)
            except MewsRateLimitError as exc:
                last_exc = exc
                wait = min(2**attempt, 30)
                logger.warning("Limite de requêtes atteinte — réessai dans %ds", wait)
                time.sleep(wait)
            except (httpx.TransportError, httpx.TimeoutException) as exc:
                last_exc = exc
                wait = min(2**attempt, 15)
                logger.warning("Erreur de transport (%s) — réessai dans %ds", exc, wait)
                time.sleep(wait)

        raise MewsAPIError(
            f"La requête vers {url} a échoué après {self._max_retries} tentatives",
            details={"last_error": str(last_exc)},
        )

    def close(self) -> None:
        """Ferme la session HTTP."""
        self._session.close()

    # ------------------------------------------------------------------ #
    # Interne
    # ------------------------------------------------------------------ #

    def _handle_response(self, resp: httpx.Response) -> dict[str, Any]:
        """Traite la réponse HTTP et lève les exceptions appropriées."""
        if resp.status_code == 429:
            raise MewsRateLimitError(
                "Limite de requêtes dépassée",
                status_code=429,
            )

        try:
            data: dict[str, Any] = resp.json()
        except Exception:
            resp.raise_for_status()
            return {}

        # Non-2xx avec une enveloppe d'erreur Mews
        if resp.status_code >= 400 and "Message" in data:
            self._raise_for_mews_error(data, resp.status_code)

        # 2xx mais le corps ne contient qu'une enveloppe d'erreur (aucune clé de données)
        if resp.status_code == 200 and "Message" in data:
            keys = set(data.keys())
            # Les enveloppes d'erreur Mews ne contiennent que Message, Details, Type
            if keys and keys <= {"Message", "Details", "Type"}:
                self._raise_for_mews_error(data, resp.status_code)

        resp.raise_for_status()
        return data

    @staticmethod
    def _raise_for_mews_error(data: dict[str, Any], status_code: int) -> None:
        """Lève l'exception Mews appropriée selon les données d'erreur."""
        msg = data.get("Message", "Erreur Mews inconnue")
        details = data.get("Details", "")
        error_type = data.get("Type", "")

        kwargs: dict[str, Any] = {
            "status_code": status_code,
            "error_code": error_type,
            "details": data,
        }

        if error_type in _AUTH_CODES or status_code == 401:
            raise MewsAuthError(msg, **kwargs)
        if error_type in _VALIDATION_CODES or status_code == 422:
            raise MewsValidationError(msg, **kwargs)
        if status_code == 404:
            raise MewsNotFoundError(msg, **kwargs)

        raise MewsAPIError(msg, **kwargs)
