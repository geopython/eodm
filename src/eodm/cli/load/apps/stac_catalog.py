import json
import os.path
import sys
from typing import Annotated
from urllib.parse import urlparse

import fsspec
import typer
from pystac import (
    Catalog,
    CatalogType,
    Collection,
    Item,
    StacIO,
)

from eodm.cli._errors import LoadError
from eodm.cli._globals import DEFAULT_EXTENT
from eodm.stac_contrib import FSSpecStacIO

app = typer.Typer(name="stac-catalog", no_args_is_help=True)

HEADERS = {"Content-Type": "application/json"}

StacIO.set_default(FSSpecStacIO)


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

    catalog.normalize_and_save(catalog_base_path)


@app.command(no_args_is_help=True)
def items(
    catalog_path: str,
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    source_profile: str | None = None,
    target_profile: str | None = None,
    chunk_size: int = 100000,
) -> None:
    """Load STAC Items to an existing STAC Catalog. Each item will be sorted to its
    collection
    """

    if not os.path.basename(catalog_path) == "catalog.json":
        catalog_path = os.path.join(catalog_path, "catalog.json")

    catalog_base_path = os.path.dirname(catalog_path)
    catalog = Catalog.from_file(catalog_path)

    protocol = urlparse(str(catalog_path)).scheme or "file"
    target_filesystem: fsspec.AbstractFileSystem = fsspec.filesystem(
        protocol, profile=target_profile
    )

    for i in items:
        item = Item.from_dict(json.loads(i))

        collection_id = item.collection_id
        if not collection_id:
            raise LoadError("No collection id found in item", item)

        collection = catalog.get_child(collection_id)

        if not collection:
            raise LoadError("No collection found with given id", collection_id)
        assert isinstance(collection, Collection)

        for asset_name, asset in item.get_assets().items():
            asset_file = asset.href.split("/")[-1]
            final_path = os.path.join(
                catalog_base_path, collection.id, item.id, asset_file
            )

            protocol = urlparse(str(asset.href)).scheme or "file"
            source_filesystem: fsspec.AbstractFileSystem = fsspec.filesystem(protocol)

            with (
                target_filesystem.open(final_path, "wb") as t,
                source_filesystem.open(asset.href) as s,
            ):
                data = s.read(chunk_size)
                while data:
                    t.write(data)
                    data = s.read(chunk_size)
            item.assets[asset_name].href = final_path

        collection.add_item(item)
        collection.update_extent_from_items()
        print(json.dumps(item.to_dict()))

    catalog.normalize_and_save(catalog_base_path)
