"""
Modèles pour les ressources physiques.
=======================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.configuration import Resource, ResourceCategory


class ResourceBlock(TypedDict, total=False):
    """Blocage de ressource."""
    Id: str
    ResourceId: str
    StartUtc: str
    EndUtc: str
    Type: str  # "Maintenance", "OutOfOrder", etc.
    Notes: NotRequired[str]
    CreatedUtc: NotRequired[str]


class ResourcesResponse(TypedDict):
    """Réponse de resources/getAll."""
    Resources: list[Resource]
    ResourceCategories: NotRequired[list[ResourceCategory]]


class ResourceCategoriesResponse(TypedDict):
    """Réponse de resourceCategories/getAll."""
    ResourceCategories: list[ResourceCategory]


class ResourceBlocksResponse(TypedDict):
    """Réponse de resourceBlocks/getAll."""
    ResourceBlocks: list[ResourceBlock]


class ResourceBlockAddResponse(TypedDict):
    """Réponse de resourceBlocks/add."""
    ResourceBlock: ResourceBlock


class ResourceUpdateResponse(TypedDict):
    """Réponse de resources/update."""
    Resource: Resource

