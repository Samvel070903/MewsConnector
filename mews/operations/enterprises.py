"""Opérations sur les établissements — comptes et données au niveau établissement."""

from __future__ import annotations

from typing import cast

from mews.models import (
    AgeCategoriesResponse,
    CancellationPoliciesResponse,
    CountersResponse,
    DepartmentsResponse,
    EnterprisesResponse,
)
from mews.operations import BaseOperations


class EnterpriseOperations(BaseOperations):
    """Opérations au niveau établissement / compte."""

    def get(self) -> EnterprisesResponse:
        """Récupère les détails de l'établissement actuel.

        Returns:
            EnterprisesResponse avec la liste ``Enterprises``.

        Référence:
            https://docs.mews.com/connector-api/operations/enterprises#get-all-enterprises
        """
        return cast(EnterprisesResponse, self._post("enterprises/getAll"))

    def get_departments(self) -> DepartmentsResponse:
        """Récupère tous les départements.

        Returns:
            DepartmentsResponse avec la liste ``Departments``.
        """
        return cast(DepartmentsResponse, self._post("departments/getAll"))

    def get_counters(self) -> CountersResponse:
        """Récupère tous les compteurs (ex. numérotation des factures).

        Returns:
            CountersResponse avec la liste ``Counters``.
        """
        return cast(CountersResponse, self._post("counters/getAll"))

    def get_age_categories(self) -> AgeCategoriesResponse:
        """Récupère les catégories d'âge.

        Returns:
            AgeCategoriesResponse avec la liste ``AgeCategories``.
        """
        return cast(AgeCategoriesResponse, self._post("ageCategories/getAll"))

    def get_cancellation_policies(self) -> CancellationPoliciesResponse:
        """Récupère les politiques d'annulation.

        Returns:
            CancellationPoliciesResponse avec la liste ``CancellationPolicies``.
        """
        return cast(CancellationPoliciesResponse, self._post("cancellationPolicies/getAll"))
