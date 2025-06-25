from datetime import datetime
from typing import Iterator, Optional

import pystac_client
from geojson_pydantic.geometries import Geometry
from owslib.ogcapi.records import Records
from pystac import Collection, Item

from .odata import ODataClient, ODataCollection, ODataProduct, ODataQuery
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
        product_types (list[str]): List of productTypes to search for

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


def extract_odata_products(
    url: str,
    collections: list[ODataCollection],
    datetime: tuple[datetime, datetime] | None = None,
    intersect_geometry: Geometry | None = None,
    online: bool = True,
    cloud_cover_less_than: int | None = None,
    name_contains: Optional[str] = None,
    name_not_contains: Optional[str] = None,
    top: int = 20,
) -> Iterator[ODataProduct]:
    """Extracts OData Products from an OData API

    Args:
        url (str): Link to OData API endpoint
        collections (list[ODataCollection]): List of collections to search for
        datetime (tuple[datetime, datetime], optional): Datetime interval to search. Defaults to None.
        intersect_geometry (Geometry, optional): Geometry to intersect. Defaults to None.
        online (bool, optional): Filter for online products. Defaults to True.
    """
    client = ODataClient(url)
    for collection in collections:
        query = ODataQuery(
            collection=collection.value,
            top=top,
            sensing_date=datetime,
            cloud_cover_less_than=cloud_cover_less_than,
            intersect_geometry=intersect_geometry,
            online=online,
            name_contains=name_contains,
            name_not_contains=name_not_contains,
        )
        for product in client.search(query):
            yield product


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
            limit=limit,
        )["features"]:
            yield record
