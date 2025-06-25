from typing import Iterator, Optional

import pystac_client
from owslib.ogcapi.records import Records
from pystac import Collection, Item

from .opensearch import OpenSearchClient, OpenSearchFeature


def extract_stac_api_items(
    url: str,
    collections: Optional[list[str]] = None,
    bbox: Optional[tuple[float, float, float, float]] = None,
    datetime_interval: Optional[str] = None,
    limit: Optional[int] = None,
    query: Optional[dict] = None,
    filter: Optional[dict] = None,
) -> Iterator[Item]:
    """Extracts STAC Items from a STAC API

    Args:
        url (str): Link to STAC API endpoint
        collections (Optional[list[str]], optional): List of collections to extract items from. Defaults to None.
        bbox (Optional[tuple[float, float, float, float]], optional): Bounding box to search. Defaults to None.
        datetime_interval (Optional[str], optional): Datetime interval to search. Defaults to None.
        limit (Optional[int], optional): Limit query to given number. Defaults to 10.
        query (Optional[dict], optional): STACAPI Query extension
        filter (Optional[dict], optional): STACAPI CQL Filter extension

    Yields:
        Iterator[Item]: pystac Items
    """

    client = pystac_client.Client.open(url)

    search = client.search(
        collections=collections,
        bbox=bbox,
        datetime=datetime_interval,
        limit=limit,
        query=query,
        filter=filter,
    )

    yield from search.item_collection()


def extract_stac_api_collections(url: str) -> Iterator[Collection]:
    """Extracts STAC Collections from a STAC API

    Args:
        url (str): Link to STAC API endpoint

    Yields:
        Iterator[Collection]: pystac Collections
    """

    client = pystac_client.Client.open(url)
    yield from client.get_collections()


def extract_opensearch_features(
    url: str, product_types: list[str], limit: int = 0
) -> Iterator[OpenSearchFeature]:
    """Extracts OpenSearch Features from an OpenSearch API

    Args:
        url (str): Link to OpenSearch API endpoint
        productTypes (list[str]): List of productTypes to search for

    Yields:
        Iterator[OpenSearchFeature]: OpenSearch Features
    """
    client = OpenSearchClient(url)

    query = {}

    # TODO: create mapper to map to STAC items
    for product_type in product_types:
        query["{eo:productType}"] = product_type
        for i, feature in enumerate(client.search(query), start=1):
            if limit and i >= limit:
                break
            yield feature


def extract_ogcapi_records_catalogs(url: str) -> Iterator[dict]:
    """Extracts OGC API Records from an OGC API Records endpoint

    Args:
        url (str): Link to OGC API Records endpoint

    Yields:
        Iterator[Item]: OGC API Records Catalogs(collections)
    """

    records = Records(url)
    for record in records.collections()["collections"]:
        yield record


def extract_ogcapi_records(
    url: str,
    catalog_ids: list[str],
    datetime_interval: str | None = None,
    bbox: list[float] | None = None,
    filter: str | None = None,
    cql: dict | None = None,
    limit: int | None = None,
) -> Iterator[dict]:
    """Extracts OGC API Records from an OGC API Records endpoint

    Args:
        url (str): Link to OGC API Records endpoint
        catalog_ids (list[str]): List of catalog/collection IDs to search for
        datetime_interval (str | None, optional): Datetime interval to search. ISO8601
            datetime or interval Defaults to None.
        bbox (list[float, float, float, float] | None, optional): Bounding box to search.
        filter (str, optional): CQL filter to apply. Defaults to None.
        cql (dict, optional): CQL JSON payload to apply. Defaults to None.
        limit (int | None, optional): Limit query to given number. Defaults to None.

    Yields:
        Iterator[Item]: OGC API Records Items
    """

    records = Records(url)
    for catalog_id in catalog_ids:
        for record in records.collection_items(
            catalog_id,
            bbox=bbox,
            datetime_=datetime_interval,
            filter=filter,
            cql=cql,
            limit=limit,
        )["features"]:
            yield record
