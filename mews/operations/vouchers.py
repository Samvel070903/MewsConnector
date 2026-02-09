"""Opérations sur les bons / codes promotionnels."""

from __future__ import annotations

from typing import Any, cast

from mews.models import (
    Voucher,
    VoucherAddResponse,
    VoucherDeleteResponse,
)
from mews.operations import BaseOperations


class VoucherOperations(BaseOperations):
    """Gestion des bons (vouchers)."""

    def get_all(
        self,
        *,
        voucher_ids: list[str] | None = None,
        service_ids: list[str] | None = None,
        page_size: int = 100,
    ) -> list[Voucher]:
        """Récupère les bons, pagination automatique.

        Returns:
            Liste de Voucher typés.
        """
        payload: dict[str, Any] = {}
        if voucher_ids:
            payload["VoucherIds"] = voucher_ids
        if service_ids:
            payload["ServiceIds"] = service_ids
        result = self._paginate("vouchers/getAll", payload, "Vouchers", page_size=page_size)
        return cast(list[Voucher], result)

    def add(
        self,
        *,
        service_id: str,
        rate_id: str,
        code: str,
        start_utc: str,
        end_utc: str,
        **extra: Any,
    ) -> VoucherAddResponse:
        """Crée un bon.

        Returns:
            VoucherAddResponse avec le Voucher créé.
        """
        return cast(VoucherAddResponse, self._post("vouchers/add", {
            "ServiceId": service_id,
            "RateId": rate_id,
            "Code": code,
            "StartUtc": start_utc,
            "EndUtc": end_utc,
            **extra,
        }))

    def delete(self, voucher_id: str) -> VoucherDeleteResponse:
        """Supprime un bon.

        Returns:
            VoucherDeleteResponse avec le résultat de la suppression.
        """
        return cast(VoucherDeleteResponse, self._post("vouchers/delete", {"VoucherId": voucher_id}))
