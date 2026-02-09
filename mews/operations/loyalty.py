"""Opérations sur les programmes de fidélité."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    LoyaltyMembership,
    LoyaltyMembershipAddResponse,
    LoyaltyProgramsResponse,
    LoyaltyTiersResponse,
)
from mews.operations import BaseOperations


class LoyaltyOperations(BaseOperations):
    """Adhésions et niveaux de fidélité."""

    def get_programs(self) -> LoyaltyProgramsResponse:
        """Récupère tous les programmes de fidélité.

        Returns:
            LoyaltyProgramsResponse avec la liste ``LoyaltyPrograms``.
        """
        return cast(LoyaltyProgramsResponse, self._post("loyaltyPrograms/getAll"))

    def get_memberships(
        self,
        *,
        customer_ids: list[str] | None = None,
        loyalty_program_ids: list[str] | None = None,
        page_size: int = 100,
    ) -> list[LoyaltyMembership]:
        """Récupère les adhésions de fidélité, pagination automatique.

        Returns:
            Liste de LoyaltyMembership typés.
        """
        payload: dict[str, Any] = {}
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if loyalty_program_ids:
            payload["LoyaltyProgramIds"] = loyalty_program_ids
        result = self._paginate("loyaltyMemberships/getAll", payload, "LoyaltyMemberships", page_size=page_size)
        return cast(list[LoyaltyMembership], result)

    def add_membership(
        self,
        *,
        customer_id: str,
        loyalty_program_id: str,
        code: str | None = None,
        **extra: Any,
    ) -> LoyaltyMembershipAddResponse:
        """Ajoute une adhésion de fidélité à un client.

        Returns:
            LoyaltyMembershipAddResponse avec l'adhésion créée.
        """
        payload: dict[str, Any] = {
            "CustomerId": customer_id,
            "LoyaltyProgramId": loyalty_program_id,
            **extra,
        }
        if code:
            payload["Code"] = code
        return cast(LoyaltyMembershipAddResponse, self._post("loyaltyMemberships/add", payload))

    def get_tiers(self, loyalty_program_id: str) -> LoyaltyTiersResponse:
        """Récupère les niveaux de fidélité d'un programme.

        Returns:
            LoyaltyTiersResponse avec la liste ``LoyaltyTiers``.
        """
        return cast(LoyaltyTiersResponse, self._post("loyaltyTiers/getAll", {"LoyaltyProgramId": loyalty_program_id}))
