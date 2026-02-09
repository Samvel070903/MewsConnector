"""
Modèles de configuration de l'établissement.
=============================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Address


class Enterprise(TypedDict, total=False):
    """Informations sur l'établissement."""
    Id: str
    Name: str
    TimeZoneIdentifier: str
    Email: NotRequired[str]
    Phone: NotRequired[str]
    WebsiteUrl: NotRequired[str]
    Address: NotRequired[Address]


class Service(TypedDict, total=False):
    """Service réservable (hébergement, spa, etc.)."""
    Id: str
    Name: str
    Type: str  # "Accommodation", "Event", "Service", etc.
    IsActive: NotRequired[bool]
    CategoryId: NotRequired[str]
    Ordering: NotRequired[int]
    StartUtc: NotRequired[str]
    EndUtc: NotRequired[str]


class ResourceCategory(TypedDict, total=False):
    """Catégorie de ressource (type de chambre)."""
    Id: str
    Name: str
    ShortName: NotRequired[str]
    Description: NotRequired[str]
    Ordering: NotRequired[int]


class Resource(TypedDict, total=False):
    """Ressource physique (chambre, espace, etc.)."""
    Id: str
    Name: str
    ResourceCategoryId: str
    IsActive: NotRequired[bool]
    State: NotRequired[str]  # "Clean", "Occupied", "OutOfOrder", etc.
    ParentResourceId: NotRequired[str]
    Notes: NotRequired[str]


class Rate(TypedDict, total=False):
    """Plan tarifaire."""
    Id: str
    Name: str
    ServiceId: str
    IsActive: NotRequired[bool]
    IsPublic: NotRequired[bool]
    StartUtc: NotRequired[str]
    EndUtc: NotRequired[str]


class Country(TypedDict, total=False):
    """Pays."""
    Code: str  # ISO 3166-1 alpha-2
    Name: str
    NativeName: NotRequired[str]


class Currency(TypedDict, total=False):
    """Devise."""
    Code: str  # ISO 4217
    Name: str
    Symbol: NotRequired[str]


class Language(TypedDict, total=False):
    """Langue."""
    Code: str  # ISO 639-1
    Name: str
    NativeName: NotRequired[str]


class TaxEnvironment(TypedDict, total=False):
    """Environnement fiscal."""
    Id: str
    Name: str
    Code: NotRequired[str]
    IsActive: NotRequired[bool]


class ConfigurationResponse(TypedDict):
    """Réponse de configuration/get."""
    Enterprise: Enterprise
    Services: list[Service]
    Resources: list[Resource]
    ResourceCategories: list[ResourceCategory]
    Rates: list[Rate]
    # Autres champs optionnels selon l'extent


class CountriesResponse(TypedDict):
    """Réponse de countries/getAll."""
    Countries: list[Country]


class CurrenciesResponse(TypedDict):
    """Réponse de currencies/getAll."""
    Currencies: list[Currency]


class LanguagesResponse(TypedDict):
    """Réponse de languages/getAll."""
    Languages: list[Language]


class TaxEnvironmentsResponse(TypedDict):
    """Réponse de taxEnvironments/getAll."""
    TaxEnvironments: list[TaxEnvironment]

