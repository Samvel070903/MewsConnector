"""Configuration et utilitaires d'environnement pour le wrapper Mews."""

from __future__ import annotations

import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

# URLs de base Mews bien connues
DEMO_URL = "https://api.mews-demo.com"
PRODUCTION_URL = "https://api.mews.com"


@dataclass(frozen=True)
class MewsConfig:
    """Conteneur de configuration immuable.

    Paramètres:
        platform_address: URL de base de l'API Mews (démo ou production).
        client_token: *ClientToken* OAuth délivré par Mews.
        access_token: *AccessToken* pour l'établissement connecté.
        client: Chaîne libre identifiant l'intégration appelante.
        request_timeout: Délai d'expiration HTTP en secondes (par défaut 30).
    """

    platform_address: str
    client_token: str
    access_token: str
    client: str = "MewsPythonConnector/1.0"
    request_timeout: float = 30.0
    max_retries: int = 3

    # Dérivé — supprime automatiquement le slash final
    @property
    def base_url(self) -> str:
        return self.platform_address.rstrip("/")

    # ------------------------------------------------------------------ #
    # Méthodes de fabrique
    # ------------------------------------------------------------------ #

    @classmethod
    def from_env(cls, dotenv_path: str | None = None, **overrides) -> "MewsConfig":
        """Construit un :class:`MewsConfig` à partir des variables d'environnement.

        Lit :
            - ``MEWS_PLATFORM_ADDRESS``
            - ``MEWS_CLIENT_TOKEN``
            - ``MEWS_ACCESS_TOKEN``
            - ``MEWS_CLIENT``  (optionnel)
            - ``MEWS_TIMEOUT`` (optionnel, par défaut 30)
        """
        load_dotenv(dotenv_path)
        return cls(
            platform_address=overrides.get("platform_address", os.environ.get("MEWS_PLATFORM_ADDRESS", DEMO_URL)),
            client_token=overrides.get("client_token", os.environ["MEWS_CLIENT_TOKEN"]),
            access_token=overrides.get("access_token", os.environ["MEWS_ACCESS_TOKEN"]),
            client=overrides.get("client", os.environ.get("MEWS_CLIENT", "MewsPythonConnector/1.0")),
            request_timeout=float(overrides.get("request_timeout", os.environ.get("MEWS_TIMEOUT", "30"))),
        )
