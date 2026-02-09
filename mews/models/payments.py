"""
Modèles pour les paiements.
============================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount


class Payment(TypedDict, total=False):
    """Paiement."""
    Id: str
    CustomerId: str
    Amount: Amount
    Type: str  # "Cash", "CreditCard", "BankTransfer", "Voucher", etc.
    State: NotRequired[str]  # "Pending", "Processed", "Failed", etc.
    CreatedUtc: NotRequired[str]
    UpdatedUtc: NotRequired[str]
    Notes: NotRequired[str]
    ExternalId: NotRequired[str]
    BillIds: NotRequired[list[str]]


class PaymentsResponse(TypedDict):
    """Réponse de payments/getAll."""
    Payments: list[Payment]
    Cursor: NotRequired[str]


class PaymentAddResponse(TypedDict):
    """Réponse de payments/add."""
    Payment: Payment

