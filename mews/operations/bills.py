"""Opérations sur les factures / notes."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import (
    Bill,
    BillCloseResponse,
    BillPdfResponse,
)
from mews.operations import BaseOperations


class BillOperations(BaseOperations):
    """Opérations sur les factures (folios/notes)."""

    def get_all(
        self,
        *,
        bill_ids: list[str] | None = None,
        customer_ids: list[str] | None = None,
        created_utc: dict[str, str] | None = None,
        closed_utc: dict[str, str] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[Bill]:
        """
        Récupère les factures avec des filtres optionnels. Pagination automatique.

        L'API Mews **exige** au moins un filtre parmi :
        BillIds, CustomerIds, CreatedUtc, ClosedUtc.

        Si **aucun** filtre n'est fourni, une fenêtre ``CreatedUtc`` par défaut
        couvrant les *days_back* derniers jours (par défaut 90) est automatiquement
        appliquée pour que l'appel API réussisse.

        Args:
            bill_ids: Filtrer par identifiants de factures.
            customer_ids: Filtrer par identifiants de clients.
            created_utc: ``{"StartUtc": "...", "EndUtc": "..."}`` — filtrer par date de création.
            closed_utc: Même format — filtrer par date de clôture.
            page_size: Taille de page (max 1000).
            days_back: Lorsqu'aucun filtre n'est fourni, remonter de ce
                nombre de jours via ``CreatedUtc`` (par défaut ``90``).

        Returns:
            Liste de Bill typés.

        Raises:
            MewsAPIError: Si aucun filtre n'est fourni et que l'application du filtre par défaut échoue.
        """
        payload: dict[str, Any] = {}
        if bill_ids:
            payload["BillIds"] = bill_ids
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if created_utc:
            payload["CreatedUtc"] = created_utc
        if closed_utc:
            payload["ClosedUtc"] = closed_utc

        # Mews exige au moins un filtre — on applique un filtre par défaut raisonnable
        _filter_keys = {
            "BillIds", "CustomerIds", "CreatedUtc", "ClosedUtc",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["CreatedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("bills/getAll", payload, "Bills", page_size=page_size)
        return cast(list[Bill], result)

    def close(self, bill_id: str) -> BillCloseResponse:
        """Clôture une facture ouverte.

        Returns:
            BillCloseResponse avec la facture clôturée.
        """
        return cast(BillCloseResponse, self._post("bills/close", {"BillId": bill_id}))

    def get_pdf(self, bill_id: str) -> BillPdfResponse:
        """Récupère une facture au format PDF (retourne des données en base64).

        Returns:
            BillPdfResponse avec les données PDF en base64.
        """
        return cast(BillPdfResponse, self._post("bills/getPdf", {"BillId": bill_id}))
