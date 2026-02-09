"""Client Mews Connector de haut niveau."""

from __future__ import annotations

import logging
from typing import Any

from mews.config import MewsConfig
from mews.transport import Transport

# Espaces de noms d'opérations
from mews.operations.configuration import ConfigurationOperations
from mews.operations.enterprises import EnterpriseOperations
from mews.operations.customers import CustomerOperations
from mews.operations.reservations import ReservationOperations
from mews.operations.services import ServiceOperations
from mews.operations.resources import ResourceOperations
from mews.operations.rates import RateOperations
from mews.operations.payments import PaymentOperations
from mews.operations.bills import BillOperations
from mews.operations.accounting import AccountingOperations
from mews.operations.companies import CompanyOperations
from mews.operations.products import ProductOperations
from mews.operations.outlets import OutletOperations
from mews.operations.orders import OrderOperations
from mews.operations.devices import DeviceOperations
from mews.operations.loyalty import LoyaltyOperations
from mews.operations.vouchers import VoucherOperations

logger = logging.getLogger("mews")


class MewsClient:
    """Point d'entrée pour interagir avec l'API Mews Connector.

    Utilisation ::

        client = MewsClient(
            platform_address="https://api.mews-demo.com",
            client_token="E87AA6...",
            access_token="C66EF7...",
            client="Mon Intégration 1.0",
        )

        config = client.configuration.get()
        customers = client.customers.get_all()

    Chaque *espace de noms* (``client.customers``, ``client.reservations``, …)
    regroupe les opérations API associées.
    """

    def __init__(
        self,
        platform_address: str | None = None,
        client_token: str | None = None,
        access_token: str | None = None,
        client: str = "MewsPythonConnector/1.0",
        request_timeout: float = 30.0,
        max_retries: int = 3,
        *,
        config: MewsConfig | None = None,
    ) -> None:
        """Initialise le client.

        Vous pouvez soit passer les paramètres directement **soit** fournir
        un :class:`MewsConfig` pré-construit via le mot-clé *config*.

        Si ni les paramètres explicites ni *config* ne sont fournis, le client
        tentera de charger depuis les variables d'environnement / ``.env``.
        """
        if config is not None:
            self._config = config
        elif client_token and access_token and platform_address:
            self._config = MewsConfig(
                platform_address=platform_address,
                client_token=client_token,
                access_token=access_token,
                client=client,
                request_timeout=request_timeout,
                max_retries=max_retries,
            )
        else:
            self._config = MewsConfig.from_env(
                platform_address=platform_address,
                client_token=client_token,
                access_token=access_token,
                client=client,
            )

        self._transport = Transport(
            base_url=self._config.base_url,
            timeout=self._config.request_timeout,
            max_retries=self._config.max_retries,
        )

        # Bloc d'authentification injecté dans chaque corps de requête
        self._auth_payload: dict[str, Any] = {
            "ClientToken": self._config.client_token,
            "AccessToken": self._config.access_token,
            "Client": self._config.client,
        }

        # ---- Espaces de noms ---- #
        self.configuration = ConfigurationOperations(self)
        self.enterprises = EnterpriseOperations(self)
        self.customers = CustomerOperations(self)
        self.reservations = ReservationOperations(self)
        self.services = ServiceOperations(self)
        self.resources = ResourceOperations(self)
        self.rates = RateOperations(self)
        self.payments = PaymentOperations(self)
        self.bills = BillOperations(self)
        self.accounting = AccountingOperations(self)
        self.companies = CompanyOperations(self)
        self.products = ProductOperations(self)
        self.outlets = OutletOperations(self)
        self.orders = OrderOperations(self)
        self.devices = DeviceOperations(self)
        self.loyalty = LoyaltyOperations(self)
        self.vouchers = VoucherOperations(self)

        logger.info("MewsClient initialisé → %s", self._config.base_url)

    # ------------------------------------------------------------------ #
    # Helpers exposés aux espaces de noms d'opérations
    # ------------------------------------------------------------------ #

    def _request(self, endpoint: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """Envoie une requête authentifiée.

        Le bloc d'authentification est **fusionné** dans *payload* automatiquement.
        """
        body = {**self._auth_payload}
        if payload:
            body.update(payload)
        return self._transport.request(endpoint, body)

    @property
    def transport(self) -> Transport:
        """Retourne l'instance de transport sous-jacente."""
        return self._transport

    @property
    def auth_payload(self) -> dict[str, Any]:
        """Retourne une copie du bloc d'authentification."""
        return dict(self._auth_payload)

    # ------------------------------------------------------------------ #
    # Gestionnaire de contexte
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Ferme la session HTTP sous-jacente."""
        self._transport.close()

    def __enter__(self) -> "MewsClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"<MewsClient url={self._config.base_url!r}>"
