"""Opérations sur les paiements."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import (
    Payment,
    PaymentAddResponse,
)
from mews.operations import BaseOperations


class PaymentOperations(BaseOperations):
    """Opérations sur les paiements."""

    def get_all(
        self,
        *,
        payment_ids: list[str] | None = None,
        account_ids: list[str] | None = None,
        bill_ids: list[str] | None = None,
        reservation_ids: list[str] | None = None,
        created_utc: dict[str, str] | None = None,
        updated_utc: dict[str, str] | None = None,
        charged_utc: dict[str, str] | None = None,
        closed_utc: dict[str, str] | None = None,
        settlement_utc: dict[str, str] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[Payment]:
        """
        Récupère les paiements avec des filtres optionnels. Pagination automatique.

        L'API Mews **exige** au moins un filtre parmi :
        PaymentIds, AccountIds, BillIds, ReservationIds, CreatedUtc, UpdatedUtc,
        ChargedUtc, ClosedUtc, SettlementUtc.

        Si **aucun** filtre n'est fourni, une fenêtre ``CreatedUtc`` par défaut
        couvrant les *days_back* derniers jours (par défaut 90) est automatiquement
        appliquée pour que l'appel API réussisse.

        Args:
            payment_ids: Filtrer par identifiants de paiements.
            account_ids: Filtrer par identifiants de comptes.
            bill_ids: Filtrer par identifiants de factures.
            reservation_ids: Filtrer par identifiants de réservations.
            created_utc: ``{"StartUtc": "...", "EndUtc": "..."}`` — filtrer par date de création.
            updated_utc: Même format — filtrer par date de mise à jour.
            charged_utc: Même format — filtrer par date de charge.
            closed_utc: Même format — filtrer par date de clôture.
            settlement_utc: Même format — filtrer par date de règlement.
            page_size: Taille de page (max 1000).
            days_back: Lorsqu'aucun filtre n'est fourni, remonter de ce
                nombre de jours via ``CreatedUtc`` (par défaut ``90``).

        Returns:
            Liste de Payment typés.

        Raises:
            MewsAPIError: Si aucun filtre n'est fourni et que l'application du filtre par défaut échoue.
        """
        payload: dict[str, Any] = {}
        if payment_ids:
            payload["PaymentIds"] = payment_ids
        if account_ids:
            payload["AccountIds"] = account_ids
        if bill_ids:
            payload["BillIds"] = bill_ids
        if reservation_ids:
            payload["ReservationIds"] = reservation_ids
        if created_utc:
            payload["CreatedUtc"] = created_utc
        if updated_utc:
            payload["UpdatedUtc"] = updated_utc
        if charged_utc:
            payload["ChargedUtc"] = charged_utc
        if closed_utc:
            payload["ClosedUtc"] = closed_utc
        if settlement_utc:
            payload["SettlementUtc"] = settlement_utc

        # Mews exige au moins un filtre — on applique un filtre par défaut raisonnable
        _filter_keys = {
            "PaymentIds", "AccountIds", "BillIds", "ReservationIds",
            "CreatedUtc", "UpdatedUtc", "ChargedUtc", "ClosedUtc", "SettlementUtc",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["CreatedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("payments/getAll", payload, "Payments", page_size=page_size)
        return cast(list[Payment], result)

    def add(
        self,
        *,
        customer_id: str,
        amount: float,
        currency: str,
        payment_type: str = "Cash",
        notes: str | None = None,
        **extra: Any,
    ) -> PaymentAddResponse:
        """Ajoute un paiement.

        Args:
            customer_id: Client propriétaire du paiement.
            amount: Montant (positif = recette).
            currency: Code ISO 4217.
            payment_type: ``Cash``, ``CreditCard``, ``BankTransfer``, etc.
            notes: Notes optionnelles.

        Returns:
            PaymentAddResponse avec le Payment créé.
        """
        payload: dict[str, Any] = {
            "CustomerId": customer_id,
            "Amount": {"Value": amount, "Currency": currency},
            "Type": payment_type,
            **extra,
        }
        if notes:
            payload["Notes"] = notes
        return cast(PaymentAddResponse, self._post("payments/add", payload))