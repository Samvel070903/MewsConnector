"""Opérations sur les points de vente (POS, F&B, etc.)."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    OutletItem,
    OutletsResponse,
)
from mews.operations import BaseOperations


class OutletOperations(BaseOperations):
    """Opérations sur les points de vente (restaurants, bars, boutiques…)."""

    def get_all(self) -> OutletsResponse:
        """Récupère tous les points de vente.

        Returns:
            OutletsResponse avec la liste ``Outlets``.
        """
        return cast(OutletsResponse, self._post("outlets/getAll"))

    def get_items(
        self,
        *,
        outlet_ids: list[str] | None = None,
        closed_utc: dict[str, str] | None = None,
        page_size: int = 100,
    ) -> list[OutletItem]:
        """Récupère les éléments de point de vente (tickets/lignes POS), pagination automatique.

        Returns:
            Liste de OutletItem typés.
        """
        payload: dict[str, Any] = {}
        if outlet_ids:
            payload["OutletIds"] = outlet_ids
        if closed_utc:
            payload["ClosedUtc"] = closed_utc
        result = self._paginate("outletItems/getAll", payload, "OutletItems", page_size=page_size)
        return cast(list[OutletItem], result)
