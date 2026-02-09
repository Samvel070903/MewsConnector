"""
Modèles pour les programmes de fidélité.
==========================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict


class LoyaltyProgram(TypedDict, total=False):
    """Programme de fidélité."""
    Id: str
    Name: str
    IsActive: NotRequired[bool]
    Description: NotRequired[str]


class LoyaltyTier(TypedDict, total=False):
    """Niveau de fidélité."""
    Id: str
    LoyaltyProgramId: str
    Name: str
    Level: NotRequired[int]
    Benefits: NotRequired[list[str]]


class LoyaltyMembership(TypedDict, total=False):
    """Adhésion de fidélité."""
    Id: str
    CustomerId: str
    LoyaltyProgramId: str
    Code: NotRequired[str]
    TierId: NotRequired[str]
    Points: NotRequired[int]
    CreatedUtc: NotRequired[str]


class LoyaltyProgramsResponse(TypedDict):
    """Réponse de loyaltyPrograms/getAll."""
    LoyaltyPrograms: list[LoyaltyProgram]


class LoyaltyTiersResponse(TypedDict):
    """Réponse de loyaltyTiers/getAll."""
    LoyaltyTiers: list[LoyaltyTier]


class LoyaltyMembershipsResponse(TypedDict):
    """Réponse de loyaltyMemberships/getAll."""
    LoyaltyMemberships: list[LoyaltyMembership]
    Cursor: NotRequired[str]


class LoyaltyMembershipAddResponse(TypedDict):
    """Réponse de loyaltyMemberships/add."""
    LoyaltyMembership: LoyaltyMembership

