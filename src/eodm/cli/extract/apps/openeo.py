import json
import sys
from datetime import datetime
from typing import Annotated

import pystac
import typer

app = typer.Typer(no_args_is_help=True, help="Extract data from openEO results")


@app.command(no_args_is_help=True)
def results(
    asset_name: str,
    results: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
):
    try:
        result = json.load(results)
    except json.decoder.JSONDecodeError:
        pass

    assets = result["assets"]

    for name, asset in assets.items():
        dt = datetime.strptime(name, "openEO_%Y-%m-%dZ.tif")
        asset = pystac.Asset.from_dict(asset)
        item = pystac.Item(
            id=asset_name,
            geometry=None,
            bbox=None,
            datetime=dt,
            properties={},
            assets={asset_name: asset},
        )

        print(json.dumps(item.to_dict()))
