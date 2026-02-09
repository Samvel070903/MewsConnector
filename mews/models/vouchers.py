"""
Modèles pour les bons (vouchers/codes promotionnels).
=======================================================
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from mews.models.base import Amount


class Voucher(TypedDict, total=False):
    """Bon (code promotionnel)."""
    Id: str
    ServiceId: str
    RateId: str
    Code: str
    StartUtc: str
    EndUtc: str
    IsActive: NotRequired[bool]
    DiscountAmount: NotRequired[Amount]
    DiscountPercent: NotRequired[float]
    UsageCount: NotRequired[int]
    MaxUsageCount: NotRequired[int]


class VouchersResponse(TypedDict):
    """Réponse de vouchers/getAll."""
    Vouchers: list[Voucher]
    Cursor: NotRequired[str]


class VoucherAddResponse(TypedDict):
    """Réponse de vouchers/add."""
    Voucher: Voucher


class VoucherDeleteResponse(TypedDict):
    """Réponse de vouchers/delete."""
    # Structure selon la documentation

