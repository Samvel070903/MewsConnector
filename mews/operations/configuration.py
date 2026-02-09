"""Opérations de configuration — ``/api/connector/v1/configuration/…``"""

from __future__ import annotations

from typing import cast

from mews.models import (
    ConfigurationResponse,
    CountriesResponse,
    CurrenciesResponse,
    LanguagesResponse,
    TaxEnvironmentsResponse,
)
from mews.operations import BaseOperations


class ConfigurationOperations(BaseOperations):
    """Accès à la configuration de l'établissement."""

    def get(self) -> ConfigurationResponse:
        """Récupère la configuration complète de l'établissement.

        Returns:
            ConfigurationResponse avec ``Enterprise``, ``Services``, ``Resources``, etc.

        Référence:
            https://docs.mews.com/connector-api/operations/configuration#get-configuration
        """
        return cast(ConfigurationResponse, self._post("configuration/get"))

    def get_countries(self) -> CountriesResponse:
        """Récupère tous les pays supportés.

        Returns:
            CountriesResponse avec la liste ``Countries``.
        """
        return cast(CountriesResponse, self._post("countries/getAll"))

    def get_currencies(self) -> CurrenciesResponse:
        """Récupère toutes les devises supportées.

        Returns:
            CurrenciesResponse avec la liste ``Currencies``.
        """
        return cast(CurrenciesResponse, self._post("currencies/getAll"))

    def get_languages(self) -> LanguagesResponse:
        """Récupère toutes les langues supportées.

        Returns:
            LanguagesResponse avec la liste ``Languages``.
        """
        return cast(LanguagesResponse, self._post("languages/getAll"))

    def get_tax_environments(self) -> TaxEnvironmentsResponse:
        """Récupère les environnements fiscaux de l'établissement.

        Returns:
            TaxEnvironmentsResponse avec la liste ``TaxEnvironments``.
        """
        return cast(TaxEnvironmentsResponse, self._post("taxEnvironments/getAll"))
