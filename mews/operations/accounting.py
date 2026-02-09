"""Opérations sur les éléments comptables / revenus."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import AccountingItem
from mews.operations import BaseOperations


class AccountingOperations(BaseOperations):
    """Éléments comptables (charges, crédits, etc.)."""

    def get_all(
        self,
        *,
        start_utc: str | None = None,
        end_utc: str | None = None,
        customer_ids: list[str] | None = None,
        bill_ids: list[str] | None = None,
        states: list[str] | None = None,
        extent: dict[str, bool] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[AccountingItem]:
        """
        Récupère les éléments comptables avec des filtres optionnels. Pagination automatique.

        L'API Mews **exige** au moins un filtre parmi :
        ConsumedUtc, CustomerIds, BillIds, States.

        Si **aucun** filtre n'est fourni, une fenêtre ``ConsumedUtc`` par défaut
        couvrant les *days_back* derniers jours (par défaut 90) est automatiquement
        appliquée pour que l'appel API réussisse.

        Args:
            start_utc: Date de début au format ISO 8601 UTC (pour ConsumedUtc).
            end_utc: Date de fin au format ISO 8601 UTC (pour ConsumedUtc).
            customer_ids: Filtrer par identifiants de clients.
            bill_ids: Filtrer par identifiants de factures.
            states: Filtrer par états (``Open``, ``Closed``, ``Inactive``).
            extent: Sous-objets à inclure (ex: ``{"Product": True}``).
            page_size: Taille de page (max 1000).
            days_back: Lorsqu'aucun filtre n'est fourni, remonter de ce
                nombre de jours via ``ConsumedUtc`` (par défaut ``90``).

        Returns:
            Liste de AccountingItem typés.

        Raises:
            MewsAPIError: Si aucun filtre n'est fourni et que l'application du filtre par défaut échoue.
        """
        payload: dict[str, Any] = {}
        if start_utc and end_utc:
            payload["ConsumedUtc"] = {"StartUtc": start_utc, "EndUtc": end_utc}
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if bill_ids:
            payload["BillIds"] = bill_ids
        if states:
            payload["States"] = states
        if extent:
            payload["Extent"] = extent

        # Mews exige au moins un filtre — on applique un filtre par défaut raisonnable
        _filter_keys = {
            "ConsumedUtc", "CustomerIds", "BillIds", "States",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["ConsumedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("accountingItems/getAll", payload, "AccountingItems", page_size=page_size)
        return cast(list[AccountingItem], result)
