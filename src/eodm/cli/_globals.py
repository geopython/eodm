from datetime import datetime

from pystac import Extent, SpatialExtent, TemporalExtent

DEFAULT_EXTENT = Extent(
    spatial=SpatialExtent.from_coordinates([[-180, -90], [180, 90]]),
    temporal=TemporalExtent.from_now(),
)

DEFAULT_DATETIME_INTERVAL = f"{datetime(1900, 1, 1)}/.."
DEFAULT_BBOX = "-180.0,-90.0,180.0, 90.0"
