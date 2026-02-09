"""
Mews Connector API — Wrapper Python Professionnel
==================================================

Utilisation ::

    from mews import MewsClient

    client = MewsClient(
        platform_address="https://api.mews-demo.com",
        client_token="...",
        access_token="...",
        client="Mon Intégration PMS 1.0",
    )
    cfg = client.configuration.get()
"""

from mews.client import MewsClient
from mews.errors import (
    MewsAPIError,
    MewsAuthError,
    MewsNotFoundError,
    MewsRateLimitError,
    MewsValidationError,
)

# Exporter les modèles pour un accès direct si nécessaire
from mews.models import *  # noqa: F403, F401

__all__ = [
    "MewsClient",
    "MewsAPIError",
    "MewsAuthError",
    "MewsNotFoundError",
    "MewsRateLimitError",
    "MewsValidationError",
    # Les modèles sont exportés via import *
]

__version__ = "1.0.0"
