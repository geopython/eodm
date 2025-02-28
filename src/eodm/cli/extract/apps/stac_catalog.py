import json
from typing import Any, Optional

import fsspec
import typer
from pystac import HREF, Catalog, StacIO

from eodm.cli._errors import ExtractError

app = typer.Typer(no_args_is_help=True, help="Extract data from a STAC Catalog")


class FSSpecStacIO(StacIO):
    """
    Extension of StacIO to allow working with different filesystems using fsspec.
    """

    def write_text(self, dest: HREF, txt: str, *args: Any, **kwargs: Any) -> None:
        if fs := kwargs.get("filesystem"):
            with fs.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)
        else:
            with fsspec.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)

    def read_text(self, source: HREF, *args: Any, **kwargs: Any) -> str:
        if fs := kwargs.get("filesystem"):
            with fs.open(source, "r", *args, **kwargs) as f:
                return f.read()
        else:
            with fsspec.open(source, "r", *args, **kwargs) as f:
                return f.read()


StacIO.set_default(FSSpecStacIO)


@app.command(no_args_is_help=True)
def collections(stac_catalog_path: str) -> None:
    """Extract collections from a STAC Catalog"""

    catalog = Catalog.from_file(stac_catalog_path)
    for collection in catalog.get_all_collections():
        print(json.dumps(collection.to_dict()))


@app.command(no_args_is_help=True)
def collection(stac_catalog_path: str, collection_id: str) -> None:
    """Extract a collection from a STAC Catalog"""

    catalog = Catalog.from_file(stac_catalog_path)
    collection = catalog.get_child(collection_id)

    if not collection:
        raise ExtractError("No collection found", collection_id)

    print(json.dumps(collection.to_dict()))


@app.command(no_args_is_help=True)
def items(
    stac_catalog_path: str,
    collection_id: Optional[str] = None,
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

    for item in items:
        print(json.dumps(item.to_dict()))
