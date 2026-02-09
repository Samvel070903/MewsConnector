"""Classe de base partagée par tous les espaces de noms d'opérations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from mews.pagination import paginate_all

if TYPE_CHECKING:
    from mews.client import MewsClient


class BaseOperations:
    """Base légère fournissant des helpers aux espaces de noms enfants."""

    def __init__(self, client: "MewsClient") -> None:
        self._client = client

    def _post(self, endpoint: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """Envoie une requête POST authentifiée."""
        return self._client._request(endpoint, payload)

    def _paginate(
        self,
        endpoint: str,
        payload: dict[str, Any],
        result_key: str,
        page_size: int = 100,
    ) -> list[dict[str, Any]]:
        """Raccourci : pagine automatiquement et retourne la liste complète."""
        body = {**self._client.auth_payload, **(payload or {})}
        return paginate_all(
            self._client.transport,
            endpoint,
            body,
            result_key,
            page_size=page_size,
        )
