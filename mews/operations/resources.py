"""Opérations sur les ressources — chambres, espaces, places de parking, etc."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    ResourceBlockAddResponse,
    ResourceBlocksResponse,
    ResourceCategoriesResponse,
    ResourceUpdateResponse,
    ResourcesResponse,
)
from mews.operations import BaseOperations


class ResourceOperations(BaseOperations):
    """CRUD pour les ressources physiques."""

    def get_all(
        self,
        *,
        resource_ids: list[str] | None = None,
        extent: dict[str, bool] | None = None,
    ) -> ResourcesResponse:
        """Récupère toutes les ressources (chambres, espaces…).

        Returns:
            ResourcesResponse avec ``Resources``, ``ResourceCategories``, etc.
        """
        payload: dict[str, Any] = {}
        if resource_ids:
            payload["ResourceIds"] = resource_ids
        if extent:
            payload["Extent"] = extent
        return cast(ResourcesResponse, self._post("resources/getAll", payload))

    def get_categories(self) -> ResourceCategoriesResponse:
        """Récupère les catégories de ressources (types de chambre).

        Returns:
            ResourceCategoriesResponse avec la liste ``ResourceCategories``.
        """
        return cast(ResourceCategoriesResponse, self._post("resourceCategories/getAll"))

    def update(self, resource_id: str, **fields: Any) -> ResourceUpdateResponse:
        """Met à jour une ressource.

        Returns:
            ResourceUpdateResponse avec la ressource mise à jour.
        """
        return cast(ResourceUpdateResponse, self._post("resources/update", {"ResourceId": resource_id, **fields}))

    def get_blocks(
        self,
        *,
        start_utc: str,
        end_utc: str,
        resource_ids: list[str] | None = None,
    ) -> ResourceBlocksResponse:
        """Récupère les blocages de ressources (hors service, maintenance…).

        Returns:
            ResourceBlocksResponse avec la liste ``ResourceBlocks``.
        """
        payload: dict[str, Any] = {"StartUtc": start_utc, "EndUtc": end_utc}
        if resource_ids:
            payload["ResourceIds"] = resource_ids
        return cast(ResourceBlocksResponse, self._post("resourceBlocks/getAll", payload))

    def add_block(
        self,
        *,
        resource_id: str,
        start_utc: str,
        end_utc: str,
        reason: str = "Maintenance",
        **extra: Any,
    ) -> ResourceBlockAddResponse:
        """Crée un blocage de ressource.

        Returns:
            ResourceBlockAddResponse avec le blocage créé.
        """
        return cast(ResourceBlockAddResponse, self._post("resourceBlocks/add", {
            "ResourceId": resource_id,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
            "Type": reason,
            **extra,
        }))

    def delete_block(self, block_id: str) -> dict[str, Any]:
        """Supprime un blocage de ressource.

        Returns:
            Réponse de confirmation (structure selon la documentation).
        """
        return self._post("resourceBlocks/delete", {"ResourceBlockId": block_id})
