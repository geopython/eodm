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
        for asset_name, asset in item.assets.items():
            if asset_name not in bands_:
                assets_rest.append(asset_name)

        for asset_name in assets_rest:
            item.assets.pop(asset_name)

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
