import json
import os.path
import sys
import threading
from datetime import datetime
from typing import Annotated, cast

import pystac
import rasterio
import rioxarray  # noqa
import typer
from odc.stac import configure_rio, load
from pandas import to_datetime
from rio_cogeo import cog_profiles, cog_translate

from ....types import BBoxType

configure_rio(cloud_defaults=True)

app = typer.Typer(no_args_is_help=True)

HEADERS = {"Content-Type": "application/json"}


@app.command(no_args_is_help=True)
def snowmap(
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    bbox: BBoxType = None,
    green_band: str = "green",
    swir_band: str = "swir16",
    scl_band: str = "scl",
    groupby: str = "solar_day",
    output_dir: str = "/tmp",
) -> None:
    """Creates snowmap images from ITEMS"""
    bands = [green_band, swir_band, scl_band]

    _bbox = None
    if bbox:
        _bbox = cast(tuple[float, float, float, float], tuple(bbox))

    items_ = []
    for line in items.readlines():
        item_dict = json.loads(line)
        item = pystac.Item.from_dict(item_dict)
        items_.append(item)

    ds = load(items_, bands=bands, bbox=_bbox, chunks={}, groupby=groupby)

    ndsi = (ds[green_band] - ds[swir_band]) / (ds[green_band] + ds[swir_band]).astype(
        "int8"
    )
    ndsi_mask = ndsi > 0.42
    cloud_mask = (ds[scl_band] == 8) | (ds[scl_band] == 9) | (ds[scl_band] == 3)
    snowmap_cloudfree = ndsi_mask.where(cloud_mask, other=0)
    for slice in snowmap_cloudfree:
        dt: datetime = to_datetime(slice.time.values).to_pydatetime()
        dt_str = dt.strftime("%Y%m%d_%H%M%S%f")

        raster_id = f"snowmap_{dt_str}"
        temp_raster_file = f"{raster_id}_temp.tiff"
        raster_file = f"{raster_id}.tiff"
        temp_raster_path = os.path.join(output_dir, temp_raster_file)
        cog = os.path.join(output_dir, raster_file)
        slice.rio.to_raster(temp_raster_path, lock=threading.Lock(), dtype="int8")

        output_profile = cog_profiles.get("lzw")
        output_profile.update(dict(BIGTIFF="IF_SAFER"))

        cog_translate(
            temp_raster_path,
            cog,
            output_profile,
            config=dict(
                GDAL_NUM_THREADS="ALL_CPUS",
                GDAL_TIFF_INTERNAL_MASK=True,
                GDAL_TIFF_OVR_BLOCKSIZE="128",
            ),
            quiet=True,
        )

        print(cog)


@app.command(no_args_is_help=True)
def ensure_cog(
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    overview_level: int = 3,
    output_dir: str = "/tmp",
) -> None:
    """Creates COG images from all assets in ITEMS"""
    output_profile = cog_profiles.get("lzw")
    output_profile.update(dict(BIGTIFF="IF_SAFER"))
    for i in items:
        item = pystac.Item.from_dict(json.loads(i))

        for asset in item.assets.values():
            file_name = asset.href.split("/")[-1]
            cog = os.path.join(output_dir, file_name)
            with rasterio.open(asset.href) as src:
                cog_translate(
                    src,
                    cog,
                    output_profile,
                    overview_level=overview_level,
                    config=dict(
                        GDAL_NUM_THREADS="ALL_CPUS",
                        GDAL_TIFF_INTERNAL_MASK=True,
                        GDAL_TIFF_OVR_BLOCKSIZE="128",
                    ),
                    quiet=True,
                )

                print(cog)
