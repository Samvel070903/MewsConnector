"""
Types de base réutilisables pour tous les modèles Mews.
=======================================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict


class Amount(TypedDict):
    """Montant avec devise."""
    Value: float
    Currency: str


class TimeInterval(TypedDict):
    """Intervalle de temps."""
    StartUtc: str  # ISO 8601
    EndUtc: str  # ISO 8601


class Address(TypedDict, total=False):
    """Adresse postale conforme à l'API Mews."""
    Id: str
    Line1: NotRequired[str]
    Line2: NotRequired[str | None]
    City: NotRequired[str]
    PostalCode: NotRequired[str]
    CountryCode: NotRequired[str]
    CountrySubdivisionCode: NotRequired[str | None]  # Code de subdivision du pays (région, état, etc.)
    State: NotRequired[str]
    Latitude: NotRequired[float | None]
    Longitude: NotRequired[float | None]


class Document(TypedDict, total=False):
    """Document (passeport, carte d'identité, visa, permis de conduire, etc.)."""
    Id: str
    Type: NotRequired[str]
    Number: NotRequired[str]
    ExpirationUtc: NotRequired[str]
    IssuanceUtc: NotRequired[str]
    IssuanceCountryCode: NotRequired[str]

