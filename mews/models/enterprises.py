"""
Modèles pour les établissements et données au niveau entreprise.
=================================================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount
from mews.models.configuration import Enterprise


class Department(TypedDict, total=False):
    """Département de l'établissement."""
    Id: str
    Name: str
    IsActive: NotRequired[bool]
    Ordering: NotRequired[int]


class Counter(TypedDict, total=False):
    """Compteur (numérotation automatique)."""
    Id: str
    Name: str
    Value: int
    Prefix: NotRequired[str]
    Suffix: NotRequired[str]


class AgeCategory(TypedDict, total=False):
    """Catégorie d'âge."""
    Id: str
    Name: str
    FromAge: NotRequired[int]
    ToAge: NotRequired[int]
    Ordering: NotRequired[int]


class CancellationPolicy(TypedDict, total=False):
    """Politique d'annulation."""
    Id: str
    Name: str
    IsDefault: NotRequired[bool]
    CancellationFee: NotRequired[Amount]
    CancellationFeeBeforeArrivalUtc: NotRequired[str]


class EnterprisesResponse(TypedDict):
    """Réponse de enterprises/getAll."""
    Enterprises: list[Enterprise]


class DepartmentsResponse(TypedDict):
    """Réponse de departments/getAll."""
    Departments: list[Department]


class CountersResponse(TypedDict):
    """Réponse de counters/getAll."""
    Counters: list[Counter]


class AgeCategoriesResponse(TypedDict):
    """Réponse de ageCategories/getAll."""
    AgeCategories: list[AgeCategory]


class CancellationPoliciesResponse(TypedDict):
    """Réponse de cancellationPolicies/getAll."""
    CancellationPolicies: list[CancellationPolicy]

