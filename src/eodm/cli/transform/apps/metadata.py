import importlib.metadata
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated

import pystac
import rasterio
import typer
from rio_stac import create_stac_item

app = typer.Typer(no_args_is_help=True)


@app.command(no_args_is_help=True)
def band_subset(
    bands: Annotated[str, typer.Argument(help="Comma separated list of bands")],
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
) -> None:
    """
    Subsets provided STAC ITEMS to only include the specified BANDS
    """
    bands_ = bands.split(",")
    for i in items:
        assets_rest = []
        item = pystac.Item.from_dict(json.loads(i))
        for band in bands_:
            if item.assets.get(band) is None:
                raise ValueError(f"Band {band} not found in item")

        for asset_name, asset in item.assets.items():
            if asset_name not in bands_:
                assets_rest.append(asset_name)

        for asset_name in assets_rest:
            item.assets.pop(asset_name)

        print(json.dumps(item.to_dict()))


@app.command(no_args_is_help=True)
def update_metadata(
    remove_earthsearch: bool = True,
    remove_canonical_link: bool = True,
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
) -> None:
    """
    Update metadata of STAC ITEMS from FILES read from STDIN.
    """
    for i in items:
        item = pystac.Item.from_dict(json.loads(i))
        item.properties["created"] = datetime.now().isoformat()
        item.properties["updated"] = datetime.now().isoformat()

        if remove_earthsearch:
            item.properties.pop("earthsearch:s3_path", None)
            item.properties.pop("earthsearch:payload_id", None)
            item.properties.pop("earthsearch:boa_offset_applied", None)

        if remove_canonical_link:
            item.links = [
                link for link in item.links if link.rel != pystac.RelType.CANONICAL
            ]

        for ext in item.stac_extensions:
            if "processing" in ext:
                item.properties["processing:software"] = {
                    "eodm": importlib.metadata.version("eodm")
                }
        print(json.dumps(item.to_dict()))


@app.command(no_args_is_help=True)
def wrap_items(
    collection: str,
    strptime_format: str,
    files: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
) -> None:
    """
    Wrap FILES in STAC items using STRPTIME_FORMAT to extract the date and assign to COLLECTION
    """
    for file in files:
        file = file.strip("\n")
        dt = datetime.strptime(file, strptime_format)
        raster_id = Path(file).stem
        with rasterio.open(file) as raster:
            item = create_stac_item(
                raster,
                dt,
                id=raster_id,
                collection=collection,
            )
            print(json.dumps(item.to_dict()))
