"""Exceptions personnalisées pour le wrapper Mews Connector."""

from __future__ import annotations

from typing import Any


class MewsAPIError(Exception):
    """Exception de base pour toutes les erreurs de l'API Mews.

    Attributs:
        status_code: Code HTTP renvoyé par l'API.
        error_code: Code d'erreur spécifique à Mews (ex. ``InvalidAccessToken``).
        message: Message d'erreur lisible renvoyé par l'API.
        details: Corps JSON complet pour le débogage.
    """

    def __init__(
        self,
        message: str = "Erreur API Mews",
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        self.details = details or {}
        super().__init__(self._format())

    def _format(self) -> str:
        parts = [self.message]
        if self.error_code:
            parts.append(f"[{self.error_code}]")
        if self.status_code:
            parts.append(f"(HTTP {self.status_code})")
        return " ".join(parts)


class MewsAuthError(MewsAPIError):
    """Levée lorsque l'authentification échoue (tokens invalides ou expirés)."""


class MewsRateLimitError(MewsAPIError):
    """Levée lorsque la limite de requêtes de l'API est dépassée (HTTP 429)."""


class MewsValidationError(MewsAPIError):
    """Levée lorsque le payload de la requête échoue à la validation côté Mews."""


class MewsNotFoundError(MewsAPIError):
    """Levée lorsqu'une ressource demandée n'existe pas (HTTP 404)."""
