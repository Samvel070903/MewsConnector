"""
Modèles pour les entreprises (profils corporatifs).
====================================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Address


class Company(TypedDict, total=False):
    """Profil entreprise."""
    Id: str
    Name: str
    TaxIdentificationNumber: NotRequired[str]
    Address: NotRequired[Address]
    Email: NotRequired[str]
    Phone: NotRequired[str]
    WebsiteUrl: NotRequired[str]
    Notes: NotRequired[str]
    CreatedUtc: NotRequired[str]
    UpdatedUtc: NotRequired[str]


class CompaniesResponse(TypedDict):
    """Réponse de companies/getAll."""
    Companies: list[Company]
    Cursor: NotRequired[str]


class CompanyAddResponse(TypedDict):
    """Réponse de companies/add."""
    Company: Company


class CompanyUpdateResponse(TypedDict):
    """Réponse de companies/update."""
    Company: Company


class CompanyDeleteResponse(TypedDict):
    """Réponse de companies/delete."""
    # Structure selon la documentation

