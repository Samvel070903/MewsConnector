"""Opérations sur les produits (extras, suppléments, etc.)."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    ProductAddToReservationResponse,
    ProductsResponse,
)
from mews.operations import BaseOperations


class ProductOperations(BaseOperations):
    """Opérations sur les produits (charges supplémentaires, extras)."""

    def get_all(self, *, service_id: str | None = None) -> ProductsResponse:
        """Récupère tous les produits.

        Args:
            service_id: Filtrer par service.

        Returns:
            ProductsResponse avec la liste ``Products``.
        """
        payload: dict[str, Any] = {}
        if service_id:
            payload["ServiceId"] = service_id
        return cast(ProductsResponse, self._post("products/getAll", payload))

    def add_to_reservation(
        self,
        *,
        reservation_id: str,
        product_id: str,
        count: int = 1,
        **extra: Any,
    ) -> ProductAddToReservationResponse:
        """Ajoute un produit à une réservation.

        Returns:
            ProductAddToReservationResponse avec la réservation mise à jour.
        """
        return cast(ProductAddToReservationResponse, self._post("reservations/addProduct", {
            "ReservationId": reservation_id,
            "ProductId": product_id,
            "Count": count,
            **extra,
        }))
