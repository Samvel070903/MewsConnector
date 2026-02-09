"""
Modèles pour les factures (folios/notes).
==========================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount


class BillItem(TypedDict, total=False):
    """Élément de facture."""
    Id: str
    ProductId: NotRequired[str]
    ServiceId: NotRequired[str]
    Name: str
    Amount: Amount
    Quantity: NotRequired[float]
    Notes: NotRequired[str]


class Bill(TypedDict, total=False):
    """Facture (folio/note)."""
    Id: str
    CustomerId: str
    Number: NotRequired[str]
    State: str  # "Open", "Closed", "Canceled"
    Total: Amount
    Items: NotRequired[list[BillItem]]
    CreatedUtc: NotRequired[str]
    ClosedUtc: NotRequired[str]
    Notes: NotRequired[str]
    ReservationIds: NotRequired[list[str]]


class BillsResponse(TypedDict):
    """Réponse de bills/getAll."""
    Bills: list[Bill]
    Cursor: NotRequired[str]


class BillCloseResponse(TypedDict):
    """Réponse de bills/close."""
    Bill: Bill


class BillPdfResponse(TypedDict):
    """Réponse de bills/getPdf."""
    Base64Data: str
    ContentType: NotRequired[str]

