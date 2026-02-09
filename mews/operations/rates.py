"""Opérations sur les tarifs et la tarification."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    RatePricingResponse,
    RateUpdatePriceResponse,
    RatesResponse,
)
from mews.operations import BaseOperations


class RateOperations(BaseOperations):
    """Opérations sur les tarifs et groupes de tarifs."""

    def get_all(self, *, service_id: str | None = None, extent: dict[str, bool] | None = None) -> RatesResponse:
        """Récupère tous les tarifs.

        Args:
            service_id: Filtrer par service.
            extent: Sous-objets à inclure.

        Returns:
            RatesResponse avec la liste ``Rates``.
        """
        payload: dict[str, Any] = {}
        if service_id:
            payload["ServiceId"] = service_id
        if extent:
            payload["Extent"] = extent
        return cast(RatesResponse, self._post("rates/getAll", payload))

    def get_pricing(
        self,
        *,
        rate_id: str,
        start_utc: str,
        end_utc: str,
    ) -> RatePricingResponse:
        """Récupère la tarification d'un tarif spécifique sur une période.

        Returns:
            RatePricingResponse avec les blocs de tarification.
        """
        return cast(RatePricingResponse, self._post("rates/getPricing", {
            "RateId": rate_id,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
        }))

    def update_price(
        self,
        *,
        rate_id: str,
        resource_category_id: str,
        price_updates: list[dict[str, Any]],
    ) -> RateUpdatePriceResponse:
        """Met à jour les prix d'un tarif.

        Args:
            rate_id: Tarif cible.
            resource_category_id: Type de chambre.
            price_updates: Liste de dicts avec ``StartUtc``, ``EndUtc``, ``Value``.

        Returns:
            RateUpdatePriceResponse avec le résultat de la mise à jour.
        """
        return cast(RateUpdatePriceResponse, self._post("rates/updatePrice", {
            "RateId": rate_id,
            "ResourceCategoryId": resource_category_id,
            "PriceUpdates": price_updates,
        }))
