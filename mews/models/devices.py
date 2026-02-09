"""
Modèles pour les appareils et commandes d'appareils.
=====================================================
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict


class Device(TypedDict, total=False):
    """Appareil (encodeur de clés, terminal, etc.)."""
    Id: str
    Name: str
    Type: str  # "KeyEncoder", "PaymentTerminal", etc.
    IsActive: NotRequired[bool]
    SerialNumber: NotRequired[str]
    Location: NotRequired[str]


class DeviceCommand(TypedDict, total=False):
    """Commande d'appareil."""
    Id: str
    DeviceId: str
    Type: str
    State: str  # "Pending", "Received", "Processing", "Processed", "Error"
    Data: NotRequired[dict[str, Any]]
    CreatedUtc: NotRequired[str]
    ProcessedUtc: NotRequired[str]
    ErrorMessage: NotRequired[str]


class DevicesResponse(TypedDict):
    """Réponse de devices/getAll."""
    Devices: list[Device]


class DeviceCommandsResponse(TypedDict):
    """Réponse de deviceCommands/getAll."""
    DeviceCommands: list[DeviceCommand]
    Cursor: NotRequired[str]


class DeviceCommandUpdateResponse(TypedDict):
    """Réponse de deviceCommands/update."""
    DeviceCommand: DeviceCommand

