"""Opérations sur les services — services réservables et disponibilité."""

from __future__ import annotations

from typing import cast

from mews.models import (
    ServiceAvailabilityResponse,
    ServicePricingResponse,
    ServicesResponse,
)
from mews.operations import BaseOperations


class ServiceOperations(BaseOperations):
    """Opérations sur les services réservables (hébergement, spa, etc.)."""

    def get_all(self) -> ServicesResponse:
        """Récupère tous les services de l'établissement.

        Returns:
            ServicesResponse avec la liste ``Services``.
        """
        return cast(ServicesResponse, self._post("services/getAll"))

    def get_availability(
        self,
        *,
        service_id: str,
        start_utc: str,
        end_utc: str,
        resource_category_id: str | None = None,
    ) -> ServiceAvailabilityResponse:
        """Récupère la disponibilité des ressources pour un service.

        Args:
            service_id: Service cible.
            start_utc: Début au format ISO-8601.
            end_utc: Fin au format ISO-8601.
            resource_category_id: Filtre optionnel par catégorie.

        Returns:
            ServiceAvailabilityResponse avec les blocs de disponibilité.
        """
        from typing import Any
        payload: dict[str, Any] = {
            "ServiceId": service_id,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
        }
        if resource_category_id:
            payload["ResourceCategoryId"] = resource_category_id
        return cast(ServiceAvailabilityResponse, self._post("services/getAvailability", payload))

    def get_pricing(
        self,
        *,
        service_id: str,
        start_utc: str,
        end_utc: str,
    ) -> ServicePricingResponse:
        """Récupère la tarification d'un service sur une période.

        Returns:
            ServicePricingResponse avec les blocs de tarification.
        """
        return cast(ServicePricingResponse, self._post("services/getPricing", {
            "ServiceId": service_id,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
        }))
