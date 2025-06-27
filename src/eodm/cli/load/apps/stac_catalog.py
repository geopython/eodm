import json
import logging
import os.path
import sys
from typing import Annotated, Optional
from urllib.parse import urlparse

import typer
from pystac import (
    Catalog,
    CatalogType,
    Collection,
    Item,
    StacIO,
)

from eodm.cli._errors import LoadError
from eodm.cli._filesystem import _get_fsspec_fs
from eodm.cli._globals import DEFAULT_EXTENT
from eodm.stac_contrib import FSSpecStacIO

app = typer.Typer(name="stac-catalog", no_args_is_help=True)

HEADERS = {"Content-Type": "application/json"}

StacIO.set_default(FSSpecStacIO)
LOGGER = logging.getLogger(__name__)


@app.callback()
def main():
    """
    Load data and metadata to a STAC catalog
    """


@app.command(no_args_is_help=True)
def catalog(catalog_path: str, id: str, description: str, title: str):
    """Create a STAC Catalog"""

    catalog = Catalog(
        id,
        description,
        title,
        catalog_type=CatalogType.ABSOLUTE_PUBLISHED,
    )

    catalog.normalize_and_save(catalog_path)


@app.command(no_args_is_help=True)
def collection(
    catalog_path: str,
    id: str,
    description: str,
    title: str,
) -> None:
    """Create and add a STAC Collection to an existing STAC Catalog"""

    if not os.path.basename(catalog_path) == "catalog.json":
        catalog_path = os.path.join(catalog_path, "catalog.json")

    catalog = Catalog.from_file(catalog_path)

    collection = Collection(
        id=id,
        description=description,
        extent=DEFAULT_EXTENT,
        title=title,
    )

    catalog.add_child(collection)
    catalog_base_path = os.path.dirname(catalog_path)
    catalog.normalize_and_save(catalog_base_path)


@app.command(no_args_is_help=True)
def collections(
    catalog_path: str,
    collections: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
) -> None:
    """Load STAC Collections to an existing STAC Catalog"""

    if not os.path.basename(catalog_path) == "catalog.json":
        catalog_path = os.path.join(catalog_path, "catalog.json")

    catalog = Catalog.from_file(catalog_path)
    catalog_base_path = os.path.dirname(catalog_path)

    for line in collections:
        collection = Collection.from_dict(json.loads(line))
        catalog.add_child(collection)

    catalog.normalize_and_save(
        catalog_base_path,
        catalog_type=CatalogType.ABSOLUTE_PUBLISHED,
        skip_unresolved=True,
    )


@app.command(no_args_is_help=True)
def items(
    catalog_path: str,
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    source_profile: Optional[str] = None,
    target_profile: Optional[str] = None,
    source_protocol: str = "file",
    chunk_size: int = 100000,
    update: bool = False,
) -> None:
    """Load STAC Items to an existing STAC Catalog. Each item will be sorted to its
    collection, and the path will be infered based on catalog_path
    """

    if not os.path.basename(catalog_path) == "catalog.json":
        catalog_path = os.path.join(catalog_path, "catalog.json")

    catalog_base_path = os.path.dirname(catalog_path)

    target_protocol = urlparse(str(catalog_path)).scheme or "file"
    source_filesystem = _get_fsspec_fs(source_protocol, profile=source_profile)
    target_filesystem = _get_fsspec_fs(target_protocol, profile=target_profile)
    catalog = Catalog.from_file(catalog_path, FSSpecStacIO(filesystem=target_filesystem))

    collections: set[Collection] = set()
    for i in items:
        item = Item.from_dict(json.loads(i))
        LOGGER.info("Loading item", extra={"id": item.id})

        collection_id = item.collection_id

        if not collection_id:
            raise LoadError("No collection id found in item", item)

        collection = catalog.get_child(collection_id)

        if not collection:
            raise LoadError("No collection found with given id", collection_id)
        assert isinstance(collection, Collection)
        collections.add(collection)

        for asset_name, asset in item.assets.items():
            LOGGER.info("Loading asset", extra={"asset": asset_name})
            asset_file = asset.href.split("/")[-1]
            final_path = os.path.join(
                catalog_base_path, collection.id, item.id, asset_file
            )

            if not target_filesystem.exists(final_path) or update:
                with (
                    source_filesystem.open(asset.href) as s,
                    target_filesystem.open(final_path, "wb") as t,
                ):
                    data = s.read(chunk_size)
                    while data:
                        t.write(data)
                        data = s.read(chunk_size)
            item.assets[asset_name].href = final_path

        collection.add_item(item)
        print(json.dumps(item.to_dict()))

    for collection in collections:
        collection.update_extent_from_items()

    catalog.normalize_and_save(
        catalog_base_path,
        catalog_type=CatalogType.ABSOLUTE_PUBLISHED,
        skip_unresolved=True,
        stac_io=FSSpecStacIO(filesystem=target_filesystem),
    )
