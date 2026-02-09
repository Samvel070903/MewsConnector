"""
Modèles pour les réservations.
===============================
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict

from mews.models.base import Amount


class Companion(TypedDict, total=False):
    """Accompagnant d'une réservation."""
    CustomerId: str
    FirstName: NotRequired[str]
    LastName: NotRequired[str]


class Reservation(TypedDict, total=False):
    """Réservation."""
    Id: str
    ServiceId: str
    CustomerId: str
    ResourceId: NotRequired[str]
    ResourceCategoryId: NotRequired[str]
    RateId: NotRequired[str]
    StartUtc: str
    EndUtc: str
    AdultCount: int
    ChildCount: int
    State: str  # "Enquired", "Requested", "Optional", "Confirmed", "Started", "Processed", "Canceled", "Deleted"
    CreatedUtc: NotRequired[str]
    UpdatedUtc: NotRequired[str]
    CancelledUtc: NotRequired[str]
    Companions: NotRequired[list[Companion]]
    Notes: NotRequired[str]
    Purpose: NotRequired[str]
    TravelPurpose: NotRequired[str]
    AssignedResourceId: NotRequired[str]
    AssignedResourceLocked: NotRequired[bool]


class ReservationsResponse(TypedDict):
    """Réponse de reservations/getAll."""
    Reservations: list[Reservation]
    Cursor: NotRequired[str]


class PricingItem(TypedDict, total=False):
    """Élément de tarification."""
    StartUtc: str
    EndUtc: str
    Amount: Amount
    Pricing: NotRequired[dict[str, Any]]  # Détails de tarification


class PricingResponse(TypedDict):
    """Réponse de reservations/price."""
    Total: Amount
    Items: NotRequired[list[PricingItem]]
    Currency: NotRequired[str]


class ReservationsAddResponse(TypedDict):
    """Réponse de reservations/add."""
    Reservations: list[Reservation]


class ReservationsUpdateResponse(TypedDict):
    """Réponse de reservations/update."""
    Reservation: Reservation


class ReservationsConfirmResponse(TypedDict):
    """Réponse de reservations/confirm."""
    Reservations: list[Reservation]


class ReservationsCancelResponse(TypedDict):
    """Réponse de reservations/cancel."""
    Reservations: list[Reservation]


class ReservationsStartResponse(TypedDict):
    """Réponse de reservations/start."""
    Reservations: list[Reservation]


class ReservationsProcessResponse(TypedDict):
    """Réponse de reservations/process."""
    Reservations: list[Reservation]


class ReservationsAssignResourceResponse(TypedDict):
    """Réponse de reservations/assignResource."""
    Reservation: Reservation


class ReservationsAddCompanionResponse(TypedDict):
    """Réponse de reservations/addCompanion."""
    Reservation: Reservation


class ReservationsDeleteCompanionResponse(TypedDict):
    """Réponse de reservations/deleteCompanion."""
    Reservation: Reservation

