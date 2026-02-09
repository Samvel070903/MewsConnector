"""
Modèles pour les tarifs et la tarification.
============================================
"""

from __future__ import annotations

from typing import Any, TypedDict

from mews.models.base import Amount
from mews.models.configuration import Rate


class RatePricingBlock(TypedDict, total=False):
    """Bloc de tarification d'un tarif."""
    StartUtc: str
    EndUtc: str
    ResourceCategoryId: str
    Amount: Amount


class RatesResponse(TypedDict):
    """Réponse de rates/getAll."""
    Rates: list[Rate]


class RatePricingResponse(TypedDict):
    """Réponse de rates/getPricing."""
    PricingBlocks: list[RatePricingBlock]


class RateUpdatePriceResponse(TypedDict):
    """Réponse de rates/updatePrice."""
    # Structure selon la documentation

