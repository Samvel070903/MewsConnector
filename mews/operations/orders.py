"""Opérations sur les commandes de services."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import (
    ServiceOrder,
    ServiceOrderAddResponse,
    ServiceOrderCancelResponse,
)
from mews.operations import BaseOperations


class OrderOperations(BaseOperations):
    """Commandes de services (services non-hébergement)."""

    def get_all(
        self,
        *,
        service_id: str | None = None,
        customer_ids: list[str] | None = None,
        states: list[str] | None = None,
        created_utc: dict[str, str] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[ServiceOrder]:
        """
        Récupère les commandes de services avec des filtres optionnels. Pagination automatique.

        L'API Mews **exige** au moins un filtre parmi :
        ServiceId, CustomerIds, States, CreatedUtc.

        Si **aucun** filtre n'est fourni, une fenêtre ``CreatedUtc`` par défaut
        couvrant les *days_back* derniers jours (par défaut 90) est automatiquement
        appliquée pour que l'appel API réussisse.

        Args:
            service_id: Filtrer par identifiant de service.
            customer_ids: Filtrer par identifiants de clients.
            states: Filtrer par états (ex: ["Pending", "Confirmed", "Started"]).
            created_utc: ``{"StartUtc": "...", "EndUtc": "..."}`` — filtrer par date de création.
            page_size: Taille de page (max 1000).
            days_back: Lorsqu'aucun filtre n'est fourni, remonter de ce
                nombre de jours via ``CreatedUtc`` (par défaut ``90``).

        Returns:
            Liste de ServiceOrder typés.

        Raises:
            MewsAPIError: Si aucun filtre n'est fourni et que l'application du filtre par défaut échoue.
        """
        payload: dict[str, Any] = {}
        if service_id:
            payload["ServiceId"] = service_id
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if states:
            payload["States"] = states
        if created_utc:
            payload["CreatedUtc"] = created_utc

        # Mews exige au moins un filtre — on applique un filtre par défaut raisonnable
        _filter_keys = {
            "ServiceId", "CustomerIds", "States", "CreatedUtc",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["CreatedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("serviceOrders/getAll", payload, "ServiceOrders", page_size=page_size)
        return cast(list[ServiceOrder], result)

    def add(self, *, service_id: str, customer_id: str, **fields: Any) -> ServiceOrderAddResponse:
        """Crée une commande de service.

        Returns:
            ServiceOrderAddResponse avec la ServiceOrder créée.
        """
        return cast(ServiceOrderAddResponse, self._post("serviceOrders/add", {
            "ServiceId": service_id,
            "CustomerId": customer_id,
            **fields,
        }))

    def cancel(self, order_id: str, reason: str = "") -> ServiceOrderCancelResponse:
        """Annule une commande de service.

        Returns:
            ServiceOrderCancelResponse avec la ServiceOrder annulée.
        """
        payload: dict[str, Any] = {"ServiceOrderId": order_id}
        if reason:
            payload["Reason"] = reason
        return cast(ServiceOrderCancelResponse, self._post("serviceOrders/cancel", payload))
