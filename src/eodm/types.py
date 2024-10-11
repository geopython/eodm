from datetime import datetime
from typing import Annotated, Any

import fsspec
from dateutil.parser import parse
from pystac import HREF, Extent, SpatialExtent, StacIO, TemporalExtent
from typer import Option

DEFAULT_EXTENT = Extent(
    spatial=SpatialExtent.from_coordinates([[-180, -90], [180, 90]]),
    temporal=TemporalExtent.from_now(),
)


class BBox:
    def __init__(self, ll_x: float, ll_y: float, ur_x: float, ur_y: float) -> None:
        self.ll_x = ll_x
        self.ll_y = ll_y
        self.ur_x = ur_x
        self.ur_y = ur_y

    def __str__(self) -> str:
        return f"BBox({self.ll_x}, {self.ll_y}, {self.ur_x}, {self.ur_y})"

    def as_tuple(self) -> tuple[float, float, float, float]:
        return (self.ll_x, self.ll_y, self.ur_x, self.ur_y)

    def as_list(self) -> list[float]:
        return [self.ll_x, self.ll_y, self.ur_x, self.ur_y]


def bbox(value: str) -> BBox:
    coords = value.split(",")
    if len(coords) != 4:
        raise ValueError("Invalid number of coordinates for bbox. Expected 4")

    ll_x, ll_y, ur_x, ur_y = [float(x) for x in coords]
    return BBox(ll_x, ll_y, ur_x, ur_y)


class DatetimeInterval:
    def __init__(self, lower: datetime, upper: datetime) -> None:
        self.lower = lower
        self.upper = upper

    def __str__(self) -> str:
        return f"{self.lower.isoformat()}/{self.upper.isoformat()}"


def datetime_interval(value: str) -> DatetimeInterval:
    dts = value.split("/")
    if not (0 < len(dts) < 3):
        raise ValueError("Invalid datetime interval")

    start_str, end_str = dts[0], dts[-1]

    match (start_str, end_str):
        case (_, ".."):
            start = parse(start_str)
            end = datetime.now()
        case ("..", _):
            start = datetime(1900, 1, 1)
            end = parse(end_str)
        case _:
            start = parse(start_str)
            end = parse(end_str)

    return DatetimeInterval(start, end)


BBoxType = Annotated[BBox | None, Option(parser=bbox, help="format: ll_x,ll_y,ur_x,ur_y")]
DateTimeIntervalType = Annotated[
    DatetimeInterval | None,
    Option(
        parser=datetime_interval,
        help="ISO format: single, start/end, start/.., ../end for open bounds",
    ),
]


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
