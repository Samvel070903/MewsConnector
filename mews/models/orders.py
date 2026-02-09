"""
Modèles pour les commandes de services.
=========================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict


class ServiceOrder(TypedDict, total=False):
    """Commande de service."""
    Id: str
    ServiceId: str
    CustomerId: str
    State: str  # "Pending", "Confirmed", "Started", "Processed", "Canceled"
    StartUtc: NotRequired[str]
    EndUtc: NotRequired[str]
    CreatedUtc: NotRequired[str]
    UpdatedUtc: NotRequired[str]
    Notes: NotRequired[str]


class ServiceOrdersResponse(TypedDict):
    """Réponse de serviceOrders/getAll."""
    ServiceOrders: list[ServiceOrder]
    Cursor: NotRequired[str]


class ServiceOrderAddResponse(TypedDict):
    """Réponse de serviceOrders/add."""
    ServiceOrder: ServiceOrder


class ServiceOrderCancelResponse(TypedDict):
    """Réponse de serviceOrders/cancel."""
    ServiceOrder: ServiceOrder

