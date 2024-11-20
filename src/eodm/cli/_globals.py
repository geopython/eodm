from pystac import Extent, SpatialExtent, TemporalExtent

DEFAULT_EXTENT = Extent(
    spatial=SpatialExtent.from_coordinates([[-180, -90], [180, 90]]),
    temporal=TemporalExtent.from_now(),
)
