"""
Modèles pour les services réservables.
=======================================
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict

from mews.models.configuration import Service


class AvailabilityBlock(TypedDict, total=False):
    """Bloc de disponibilité."""
    ResourceId: str
    StartUtc: str
    EndUtc: str
    AvailableCount: int
    TotalCount: NotRequired[int]


class ServicesResponse(TypedDict):
    """Réponse de services/getAll."""
    Services: list[Service]


class ServiceAvailabilityResponse(TypedDict):
    """Réponse de services/getAvailability."""
    AvailabilityBlocks: list[AvailabilityBlock]


class ServicePricingResponse(TypedDict):
    """Réponse de services/getPricing."""
    PricingBlocks: NotRequired[list[dict[str, Any]]]
    # Structure détaillée selon la documentation

