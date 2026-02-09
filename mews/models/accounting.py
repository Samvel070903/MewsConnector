"""
Modèles pour les éléments comptables.
======================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount


class AccountingItem(TypedDict, total=False):
    """Élément comptable."""
    Id: str
    Type: str  # "Charge", "Credit", etc.
    State: str  # "Open", "Closed", "Inactive"
    Amount: Amount
    ConsumedUtc: NotRequired[str]
    CreatedUtc: NotRequired[str]
    CustomerId: NotRequired[str]
    BillId: NotRequired[str]
    ProductId: NotRequired[str]
    ServiceId: NotRequired[str]
    Notes: NotRequired[str]


class AccountingItemsResponse(TypedDict):
    """Réponse de accountingItems/getAll."""
    AccountingItems: list[AccountingItem]
    Cursor: NotRequired[str]

