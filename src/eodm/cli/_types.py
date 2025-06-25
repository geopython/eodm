from datetime import datetime
from enum import Enum
from typing import Annotated, Iterator

from dateutil.parser import parse
from typer import Option


class BBox:
    def __init__(self, ll_x: float, ll_y: float, ur_x: float, ur_y: float) -> None:
        self.ll_x = ll_x
        self.ll_y = ll_y
        self.ur_x = ur_x
        self.ur_y = ur_y

    def __str__(self) -> str:
        return f"{self.ll_x},{self.ll_y},{self.ur_x},{self.ur_y}"

    def __iter__(self) -> Iterator[float]:
        yield from (self.ll_x, self.ll_y, self.ur_x, self.ur_y)


def bbox(value: str) -> BBox:
    coords = value.split(",")
    if len(coords) != 4:
        raise ValueError(
            f"Invalid number of coordinates for bbox. Expected 4, got {len(coords)}"
        )

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


class Output(str, Enum):
    default = "default"
    json = "json"
    id = "id"


BBoxType = Annotated[
    BBox | str,
    Option("--bbox", "-b", parser=bbox, help="WGS 84 format:minx,miny,maxx,maxy"),
]
DateTimeIntervalType = Annotated[
    DatetimeInterval | str,
    Option(
        "--datetime-interval",
        "-d",
        parser=datetime_interval,
        help="ISO format: single, start/end, start/.., ../end for open bounds",
    ),
]
OutputType = Annotated[
    Output, Option("--output", "-o", help="Output format. Default to STDOUT multiline")
]
