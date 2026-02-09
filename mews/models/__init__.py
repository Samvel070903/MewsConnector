"""
Module de modèles de données pour l'API Mews Connector.
========================================================

Ce module organise tous les modèles TypedDict en sous-modules pour une meilleure
maintenabilité, tout en conservant la compatibilité avec les imports existants.

Tous les modèles sont réexportés depuis ce module pour que les imports
`from mews.models import ...` continuent de fonctionner.
"""

from __future__ import annotations

# Import de tous les modèles depuis les sous-modules
from mews.models.base import (
    Address,
    Amount,
    Document,
    TimeInterval,
)
from mews.models.configuration import (
    ConfigurationResponse,
    CountriesResponse,
    Country,
    CurrenciesResponse,
    Currency,
    Enterprise,
    Language,
    LanguagesResponse,
    Rate,
    Resource,
    ResourceCategory,
    Service,
    TaxEnvironment,
    TaxEnvironmentsResponse,
)
from mews.models.enterprises import (
    AgeCategoriesResponse,
    AgeCategory,
    CancellationPoliciesResponse,
    CancellationPolicy,
    CountersResponse,
    Counter,
    DepartmentsResponse,
    Department,
    EnterprisesResponse,
)
from mews.models.customers import (
    Customer,
    CustomerAddResponse,
    CustomerInput,
    CustomerMergeResponse,
    CustomerSearchResponse,
    CustomerSearchResult,
    CustomerUpdateInput,
    CustomerUpdateResponse,
    CustomersResponse,
)
from mews.models.reservations import (
    Companion,
    PricingItem,
    PricingResponse,
    Reservation,
    ReservationsAddCompanionResponse,
    ReservationsAddResponse,
    ReservationsAssignResourceResponse,
    ReservationsCancelResponse,
    ReservationsConfirmResponse,
    ReservationsDeleteCompanionResponse,
    ReservationsProcessResponse,
    ReservationsResponse,
    ReservationsStartResponse,
    ReservationsUpdateResponse,
)
from mews.models.services import (
    AvailabilityBlock,
    ServiceAvailabilityResponse,
    ServicePricingResponse,
    ServicesResponse,
)
from mews.models.resources import (
    ResourceBlock,
    ResourceBlockAddResponse,
    ResourceBlocksResponse,
    ResourceCategoriesResponse,
    ResourceUpdateResponse,
    ResourcesResponse,
)
from mews.models.rates import (
    RatePricingBlock,
    RatePricingResponse,
    RateUpdatePriceResponse,
    RatesResponse,
)
# Rate est déjà exporté depuis configuration
from mews.models.payments import (
    Payment,
    PaymentAddResponse,
    PaymentsResponse,
)
from mews.models.bills import (
    Bill,
    BillCloseResponse,
    BillItem,
    BillPdfResponse,
    BillsResponse,
)
from mews.models.accounting import (
    AccountingItem,
    AccountingItemsResponse,
)
from mews.models.companies import (
    Company,
    CompanyAddResponse,
    CompanyDeleteResponse,
    CompaniesResponse,
    CompanyUpdateResponse,
)
from mews.models.products import (
    Product,
    ProductAddToReservationResponse,
    ProductsResponse,
)
from mews.models.outlets import (
    Outlet,
    OutletItem,
    OutletItemsResponse,
    OutletsResponse,
)
from mews.models.orders import (
    ServiceOrder,
    ServiceOrderAddResponse,
    ServiceOrderCancelResponse,
    ServiceOrdersResponse,
)
from mews.models.devices import (
    Device,
    DeviceCommand,
    DeviceCommandUpdateResponse,
    DeviceCommandsResponse,
    DevicesResponse,
)
from mews.models.loyalty import (
    LoyaltyMembership,
    LoyaltyMembershipAddResponse,
    LoyaltyMembershipsResponse,
    LoyaltyProgram,
    LoyaltyProgramsResponse,
    LoyaltyTier,
    LoyaltyTiersResponse,
)
from mews.models.vouchers import (
    Voucher,
    VoucherAddResponse,
    VoucherDeleteResponse,
    VouchersResponse,
)

# Export de tous les modèles pour compatibilité avec les imports existants
__all__ = [
    # Types de base
    "Amount",
    "TimeInterval",
    "Address",
    "Document",
    # Configuration
    "Enterprise",
    "Service",
    "ResourceCategory",
    "Resource",
    "Rate",
    "Country",
    "Currency",
    "Language",
    "TaxEnvironment",
    "ConfigurationResponse",
    "CountriesResponse",
    "CurrenciesResponse",
    "LanguagesResponse",
    "TaxEnvironmentsResponse",
    # Enterprises
    "Department",
    "Counter",
    "AgeCategory",
    "CancellationPolicy",
    "EnterprisesResponse",
    "DepartmentsResponse",
    "CountersResponse",
    "AgeCategoriesResponse",
    "CancellationPoliciesResponse",
    # Customers
    "Customer",
    "CustomersResponse",
    "CustomerSearchResult",
    "CustomerSearchResponse",
    "CustomerAddResponse",
    "CustomerUpdateResponse",
    "CustomerMergeResponse",
    "CustomerInput",
    "CustomerUpdateInput",
    # Reservations
    "Companion",
    "Reservation",
    "ReservationsResponse",
    "PricingItem",
    "PricingResponse",
    "ReservationsAddResponse",
    "ReservationsUpdateResponse",
    "ReservationsConfirmResponse",
    "ReservationsCancelResponse",
    "ReservationsStartResponse",
    "ReservationsProcessResponse",
    "ReservationsAssignResourceResponse",
    "ReservationsAddCompanionResponse",
    "ReservationsDeleteCompanionResponse",
    # Services
    "AvailabilityBlock",
    "ServicesResponse",
    "ServiceAvailabilityResponse",
    "ServicePricingResponse",
    # Resources
    "ResourceBlock",
    "ResourcesResponse",
    "ResourceCategoriesResponse",
    "ResourceBlocksResponse",
    "ResourceBlockAddResponse",
    "ResourceUpdateResponse",
    # Rates
    "RatePricingBlock",
    "RatesResponse",
    "RatePricingResponse",
    "RateUpdatePriceResponse",
    # Payments
    "Payment",
    "PaymentsResponse",
    "PaymentAddResponse",
    # Bills
    "BillItem",
    "Bill",
    "BillsResponse",
    "BillCloseResponse",
    "BillPdfResponse",
    # Accounting
    "AccountingItem",
    "AccountingItemsResponse",
    # Companies
    "Company",
    "CompaniesResponse",
    "CompanyAddResponse",
    "CompanyUpdateResponse",
    "CompanyDeleteResponse",
    # Products
    "Product",
    "ProductsResponse",
    "ProductAddToReservationResponse",
    # Outlets
    "Outlet",
    "OutletItem",
    "OutletsResponse",
    "OutletItemsResponse",
    # Orders
    "ServiceOrder",
    "ServiceOrdersResponse",
    "ServiceOrderAddResponse",
    "ServiceOrderCancelResponse",
    # Devices
    "Device",
    "DeviceCommand",
    "DevicesResponse",
    "DeviceCommandsResponse",
    "DeviceCommandUpdateResponse",
    # Loyalty
    "LoyaltyProgram",
    "LoyaltyTier",
    "LoyaltyMembership",
    "LoyaltyProgramsResponse",
    "LoyaltyTiersResponse",
    "LoyaltyMembershipsResponse",
    "LoyaltyMembershipAddResponse",
    # Vouchers
    "Voucher",
    "VouchersResponse",
    "VoucherAddResponse",
    "VoucherDeleteResponse",
]

