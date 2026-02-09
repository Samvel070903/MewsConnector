"""Opérations sur les réservations."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import (
    PricingResponse,
    Reservation,
    ReservationsAddCompanionResponse,
    ReservationsAddResponse,
    ReservationsAssignResourceResponse,
    ReservationsCancelResponse,
    ReservationsConfirmResponse,
    ReservationsDeleteCompanionResponse,
    ReservationsProcessResponse,
    ReservationsStartResponse,
    ReservationsUpdateResponse,
)
from mews.operations import BaseOperations


class ReservationOperations(BaseOperations):
    """CRUD et recherche de réservations."""

    def get_all(
        self,
        *,
        reservation_ids: list[str] | None = None,
        customer_ids: list[str] | None = None,
        service_ids: list[str] | None = None,
        resource_ids: list[str] | None = None,
        states: list[str] | None = None,
        start_utc: dict[str, str] | None = None,
        end_utc: dict[str, str] | None = None,
        created_utc: dict[str, str] | None = None,
        updated_utc: dict[str, str] | None = None,
        extent: dict[str, bool] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[Reservation]:
        """Récupère les réservations avec des filtres optionnels. Pagination automatique.

        Si **aucun** filtre temporel/identifiant n'est fourni, une fenêtre
        ``UpdatedUtc`` par défaut couvrant les *days_back* derniers jours
        (par défaut 90) est utilisée.

        États : ``Enquired``, ``Requested``, ``Optional``, ``Confirmed`",
        ``Started``, ``Processed``, ``Canceled``, ``Deleted``.

        Returns:
            Liste de Reservation typés.
        """
        payload: dict[str, Any] = {}
        if reservation_ids:
            payload["ReservationIds"] = reservation_ids
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if service_ids:
            payload["ServiceIds"] = service_ids
        if resource_ids:
            payload["ResourceIds"] = resource_ids
        if states:
            payload["States"] = states
        if start_utc:
            payload["StartUtc"] = start_utc
        if end_utc:
            payload["EndUtc"] = end_utc
        if created_utc:
            payload["CreatedUtc"] = created_utc
        if updated_utc:
            payload["UpdatedUtc"] = updated_utc
        if extent:
            payload["Extent"] = extent

        # Mews exige au moins un filtre
        _filter_keys = {
            "ReservationIds", "CustomerIds", "ServiceIds", "ResourceIds",
            "StartUtc", "EndUtc", "CreatedUtc", "UpdatedUtc",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["UpdatedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("reservations/getAll", payload, "Reservations", page_size=page_size)
        return cast(list[Reservation], result)

    def get_by_ids(self, ids: list[str]) -> list[Reservation]:
        """Raccourci : récupère des réservations par leurs identifiants."""
        return self.get_all(reservation_ids=ids)

    def price(
        self,
        *,
        service_id: str,
        start_utc: str,
        end_utc: str,
        adult_count: int = 1,
        child_count: int = 0,
        rate_id: str | None = None,
        resource_category_id: str | None = None,
        **extra: Any,
    ) -> PricingResponse:
        """Calcule le prix d'une réservation sans créer de réservation.

        Returns:
            PricingResponse avec la ventilation tarifaire.
        """
        payload: dict[str, Any] = {
            "ServiceId": service_id,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
            "AdultCount": adult_count,
            "ChildCount": child_count,
            **extra,
        }
        if rate_id:
            payload["RateId"] = rate_id
        if resource_category_id:
            payload["ResourceCategoryId"] = resource_category_id

        return cast(PricingResponse, self._post("reservations/price", payload))

    def add(self, *, service_id: str, reservations: list[dict[str, Any]]) -> ReservationsAddResponse:
        """Crée une ou plusieurs réservations.

        Args:
            service_id: L'identifiant du service réservable.
            reservations: Liste de dicts de données de réservation, contenant
                au minimum ``StartUtc``, ``EndUtc``, ``AdultCount`` et
                ``CustomerId``.

        Returns:
            ReservationsAddResponse avec les réservations créées.
        """
        return cast(ReservationsAddResponse, self._post("reservations/add", {
            "ServiceId": service_id,
            "Reservations": reservations,
        }))

    def update(self, reservation_id: str, **fields: Any) -> ReservationsUpdateResponse:
        """Met à jour une réservation existante.

        Passez les noms de champs PascalCase de Mews en arguments nommés.

        Returns:
            ReservationsUpdateResponse avec la réservation mise à jour.
        """
        return cast(ReservationsUpdateResponse, self._post("reservations/update", {"ReservationId": reservation_id, **fields}))

    def confirm(self, reservation_ids: list[str]) -> ReservationsConfirmResponse:
        """Confirme une ou plusieurs réservations.

        Returns:
            ReservationsConfirmResponse avec les réservations confirmées.
        """
        return cast(ReservationsConfirmResponse, self._post("reservations/confirm", {"ReservationIds": reservation_ids}))

    def cancel(self, reservation_ids: list[str], reason: str = "") -> ReservationsCancelResponse:
        """Annule une ou plusieurs réservations.

        Returns:
            ReservationsCancelResponse avec les réservations annulées.
        """
        payload: dict[str, Any] = {"ReservationIds": reservation_ids}
        if reason:
            payload["Reason"] = reason
        return cast(ReservationsCancelResponse, self._post("reservations/cancel", payload))

    def start(self, reservation_ids: list[str]) -> ReservationsStartResponse:
        """Démarre (check-in) des réservations.

        Returns:
            ReservationsStartResponse avec les réservations démarrées.
        """
        return cast(ReservationsStartResponse, self._post("reservations/start", {"ReservationIds": reservation_ids}))

    def process(self, reservation_ids: list[str]) -> ReservationsProcessResponse:
        """Traite (check-out) des réservations.

        Returns:
            ReservationsProcessResponse avec les réservations traitées.
        """
        return cast(ReservationsProcessResponse, self._post("reservations/process", {"ReservationIds": reservation_ids}))

    def assign_resource(self, reservation_id: str, resource_id: str) -> ReservationsAssignResourceResponse:
        """Assigne une ressource spécifique (chambre) à une réservation.

        Returns:
            ReservationsAssignResourceResponse avec la réservation mise à jour.
        """
        return cast(ReservationsAssignResourceResponse, self._post("reservations/assignResource", {
            "ReservationId": reservation_id,
            "ResourceId": resource_id,
        }))

    def add_companion(self, reservation_id: str, customer_id: str) -> ReservationsAddCompanionResponse:
        """Ajoute un accompagnant à une réservation.

        Returns:
            ReservationsAddCompanionResponse avec la réservation mise à jour.
        """
        return cast(ReservationsAddCompanionResponse, self._post("reservations/addCompanion", {
            "ReservationId": reservation_id,
            "CustomerId": customer_id,
        }))

    def delete_companion(self, reservation_id: str, customer_id: str) -> ReservationsDeleteCompanionResponse:
        """Supprime un accompagnant d'une réservation.

        Returns:
            ReservationsDeleteCompanionResponse avec la réservation mise à jour.
        """
        return cast(ReservationsDeleteCompanionResponse, self._post("reservations/deleteCompanion", {
            "ReservationId": reservation_id,
            "CustomerId": customer_id,
        }))
