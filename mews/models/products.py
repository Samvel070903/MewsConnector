"""
Modèles pour les produits (extras, suppléments).
=================================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount
from mews.models.reservations import Reservation


class Product(TypedDict, total=False):
    """Produit (extra, supplément)."""
    Id: str
    Name: str
    ServiceId: NotRequired[str]
    Price: Amount
    IsActive: NotRequired[bool]
    CategoryId: NotRequired[str]
    Description: NotRequired[str]


class ProductsResponse(TypedDict):
    """Réponse de products/getAll."""
    Products: list[Product]


class ProductAddToReservationResponse(TypedDict):
    """Réponse de reservations/addProduct."""
    Reservation: Reservation

