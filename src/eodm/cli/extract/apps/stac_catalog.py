from typing import Annotated, Optional

import typer
from pystac import Catalog, StacIO

from eodm.cli._errors import ExtractError
from eodm.cli._serialization import serialize
from eodm.cli._types import Output, OutputType
from eodm.stac_contrib import FSSpecStacIO

app = typer.Typer(no_args_is_help=True, help="Extract data from a STAC Catalog")


StacIO.set_default(FSSpecStacIO)


@app.command(no_args_is_help=True)
def collections(
    stac_catalog_path: str,
    output: OutputType = Output.default,
    skip_collection: Annotated[
        Optional[list[str]],
        typer.Option(
            help="Skip collections. Can pass multiple --skip-collection col1 --skip-collection col2"
        ),
    ] = None,
) -> None:
    """Extract collections from a STAC Catalog"""

    catalog = Catalog.from_file(stac_catalog_path)

    if skip_collection:
        collections = [
            collection
            for collection in catalog.get_all_collections()
            if collection.id not in skip_collection
        ]
    else:
        collections = list(catalog.get_all_collections())
    serialize(collections, output_type=output)


@app.command(no_args_is_help=True)
def collection(
    stac_catalog_path: str,
    collection_id: str,
    output: OutputType = Output.default,
) -> None:
    """Extract a collection from a STAC Catalog"""

    catalog = Catalog.from_file(stac_catalog_path)
    collection = catalog.get_child(collection_id)

    if not collection:
        raise ExtractError("No collection found", collection_id)

    serialize([collection], output_type=output)


@app.command(no_args_is_help=True)
def items(
    stac_catalog_path: str,
    collection_id: Optional[str] = None,
    output: OutputType = Output.default,
) -> None:
    """Extract items from a STAC Catalog"""

    catalog = Catalog.from_file(stac_catalog_path)
    if collection_id:
        collection = catalog.get_child(collection_id)

        if not collection:
            raise ExtractError("No collection found", collection_id)

        items = collection.get_items()
    else:
        items = catalog.get_items(recursive=True)

    serialize(items, output_type=output)
