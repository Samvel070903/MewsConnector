"""Utilitaires de pagination pour l'API Mews Connector.

De nombreux endpoints Mews acceptent un bloc ``Limitation`` ::

    {
        "Limitation": {
            "Count": 100,
            "Cursor": "<chaîne_opaque>"
        }
    }

et renvoient le curseur suivant dans la réponse pour permettre l'itération.
"""

from __future__ import annotations

import logging
from typing import Any, Generator, TYPE_CHECKING

if TYPE_CHECKING:
    from mews.transport import Transport

logger = logging.getLogger("mews.pagination")

DEFAULT_PAGE_SIZE = 100


def paginate(
    transport: "Transport",
    endpoint: str,
    base_payload: dict[str, Any],
    *,
    page_size: int = DEFAULT_PAGE_SIZE,
    result_key: str | None = None,
) -> Generator[dict[str, Any], None, None]:
    """Pagine automatiquement un endpoint Mews supportant ``Limitation``.

    Produit une **page** (dict de réponse complète) à la fois. L'appelant
    peut consommer les pages ou utiliser :func:`paginate_all` pour simplifier.

    Args:
        transport: Instance active de :class:`Transport`.
        endpoint: Chemin du endpoint API.
        base_payload: Corps JSON *sans* Limitation (sera ajouté automatiquement).
        page_size: Nombre d'enregistrements par page (max généralement 1000).
        result_key: Si fourni, arrête quand la liste de cette clé est vide.
    """
    cursor: str | None = None

    while True:
        payload = {**base_payload, "Limitation": {"Count": page_size}}
        if cursor:
            payload["Limitation"]["Cursor"] = cursor

        data = transport.request(endpoint, payload)
        yield data

        cursor = data.get("Cursor")
        if not cursor:
            break

        # Sortie anticipée lorsque le jeu de résultats est vide
        if result_key and not data.get(result_key):
            break


def paginate_all(
    transport: "Transport",
    endpoint: str,
    base_payload: dict[str, Any],
    result_key: str,
    *,
    page_size: int = DEFAULT_PAGE_SIZE,
) -> list[dict[str, Any]]:
    """Collecte **tous** les éléments de toutes les pages en une seule liste.

    Args:
        transport: Transport actif.
        endpoint: Endpoint API.
        base_payload: Corps JSON de base.
        result_key: Clé dans la réponse contenant la liste d'enregistrements.
        page_size: Enregistrements par page.

    Returns:
        Liste fusionnée de tous les éléments.
    """
    items: list[dict[str, Any]] = []
    for page in paginate(transport, endpoint, base_payload, page_size=page_size, result_key=result_key):
        items.extend(page.get(result_key, []))
    return items
