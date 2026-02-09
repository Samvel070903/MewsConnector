"""
Modèles pour les points de vente (POS, F&B).
==============================================
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict

from mews.models.base import Amount


class Outlet(TypedDict, total=False):
    """Point de vente."""
    Id: str
    Name: str
    Type: str  # "Restaurant", "Bar", "Shop", etc.
    IsActive: NotRequired[bool]
    DepartmentId: NotRequired[str]


class OutletItem(TypedDict, total=False):
    """Élément de point de vente (ticket/ligne POS)."""
    Id: str
    OutletId: str
    CustomerId: NotRequired[str]
    Total: Amount
    Items: NotRequired[list[dict[str, Any]]]
    CreatedUtc: NotRequired[str]
    ClosedUtc: NotRequired[str]
    State: NotRequired[str]


class OutletsResponse(TypedDict):
    """Réponse de outlets/getAll."""
    Outlets: list[Outlet]


class OutletItemsResponse(TypedDict):
    """Réponse de outletItems/getAll."""
    OutletItems: list[OutletItem]
    Cursor: NotRequired[str]

