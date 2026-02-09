"""Opérations sur les entreprises (profils corporatifs)."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    Company,
    CompanyAddResponse,
    CompanyDeleteResponse,
    CompanyUpdateResponse,
)
from mews.operations import BaseOperations


class CompanyOperations(BaseOperations):
    """CRUD pour les profils entreprise / corporatifs."""

    def get_all(
        self,
        *,
        company_ids: list[str] | None = None,
        names: list[str] | None = None,
        page_size: int = 100,
    ) -> list[Company]:
        """Récupère les entreprises, pagination automatique.

        Returns:
            Liste de Company typés.
        """
        payload: dict[str, Any] = {}
        if company_ids:
            payload["CompanyIds"] = company_ids
        if names:
            payload["Names"] = names
        result = self._paginate("companies/getAll", payload, "Companies", page_size=page_size)
        return cast(list[Company], result)

    def add(self, *, name: str, **extra: Any) -> CompanyAddResponse:
        """Crée une entreprise.

        Returns:
            CompanyAddResponse avec la Company créée.
        """
        return cast(CompanyAddResponse, self._post("companies/add", {"Name": name, **extra}))

    def update(self, company_id: str, **fields: Any) -> CompanyUpdateResponse:
        """Met à jour une entreprise.

        Returns:
            CompanyUpdateResponse avec la Company mise à jour.
        """
        return cast(CompanyUpdateResponse, self._post("companies/update", {"CompanyId": company_id, **fields}))

    def delete(self, company_id: str) -> CompanyDeleteResponse:
        """Supprime une entreprise.

        Returns:
            CompanyDeleteResponse avec le résultat de la suppression.
        """
        return cast(CompanyDeleteResponse, self._post("companies/delete", {"CompanyId": company_id}))
