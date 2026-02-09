"""Opérations d'intégration d'appareils (encodeurs de clés, terminaux de paiement…)."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    DeviceCommand,
    DeviceCommandUpdateResponse,
    DevicesResponse,
)
from mews.operations import BaseOperations


class DeviceOperations(BaseOperations):
    """Commandes d'appareils et intégration."""

    def get_all(self) -> DevicesResponse:
        """Récupère tous les appareils enregistrés.

        Returns:
            DevicesResponse avec la liste ``Devices``.
        """
        return cast(DevicesResponse, self._post("devices/getAll"))

    def get_commands(
        self,
        *,
        device_ids: list[str] | None = None,
        states: list[str] | None = None,
        created_utc: dict[str, str] | None = None,
        page_size: int = 100,
    ) -> list[DeviceCommand]:
        """Récupère les commandes d'appareils, pagination automatique.

        États : ``Pending``, ``Received``, ``Processing``, ``Processed``, ``Error``.

        Returns:
            Liste de DeviceCommand typés.
        """
        payload: dict[str, Any] = {}
        if device_ids:
            payload["DeviceIds"] = device_ids
        if states:
            payload["States"] = states
        if created_utc:
            payload["CreatedUtc"] = created_utc
        result = self._paginate("deviceCommands/getAll", payload, "DeviceCommands", page_size=page_size)
        return cast(list[DeviceCommand], result)

    def update_command(self, command_id: str, state: str, **extra: Any) -> DeviceCommandUpdateResponse:
        """Met à jour l'état d'une commande d'appareil.

        Args:
            command_id: L'identifiant de la commande.
            state: Nouvel état (``Processing``, ``Processed``, ``Error``).

        Returns:
            DeviceCommandUpdateResponse avec la commande mise à jour.
        """
        return cast(DeviceCommandUpdateResponse, self._post("deviceCommands/update", {
            "DeviceCommandId": command_id,
            "State": state,
            **extra,
        }))
