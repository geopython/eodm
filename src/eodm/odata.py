from datetime import datetime
from enum import Enum
from typing import Annotated, Iterator

import httpx
from geojson_pydantic.geometries import Geometry
from pydantic import BaseModel, Field


class ODataCollection(Enum):
    SENTINEL_1 = "SENTINEL-1"
    SENTINEL_2 = "SENTINEL-2"
    SENTINEL_3 = "SENTINEL-3"
    SENTINEL_5P = "SENTINEL-5P"
    SENTINEL_6 = "SENTINEL-6"
    SENTINEL_1_RTC = "SENTINEL-1-RTC"
    GLOBAL_MOSAICS = "GLOBAL-MOSAICS"
    SMOS = "SMOS"
    ENVISAT = "ENVISAT"
    LANDSAT_5 = "LANDSAT-5"
    LANDSAT_7 = "LANDSAT-7"
    LANDSAT_8 = "LANDSAT-8"
    COP_DEM = "COP-DEM"
    TERRAAQUA = "TERRAAQUA"
    S2GLC = "S2GLC"
    CCM = "CCM"


class ODataChecksum(BaseModel):
    value: Annotated[str, Field(alias="Value")]
    algorithm: Annotated[str, Field(alias="Algorithm")]
    checksum_date: Annotated[str, Field(alias="ChecksumDate")]


class ODataContentDate(BaseModel):
    start: Annotated[str, Field(alias="Start")]
    end: Annotated[str, Field(alias="End")]


class ODataProduct(BaseModel):
    media_content_type: Annotated[str, Field(alias="@odata.mediaContentType")]
    id: Annotated[str, Field(alias="Id")]
    name: Annotated[str, Field(alias="Name")]
    content_type: Annotated[str, Field(alias="ContentType")]
    content_length: Annotated[int, Field(alias="ContentLength")]
    origin_date: Annotated[str, Field(alias="OriginDate")]
    publication_date: Annotated[str, Field(alias="PublicationDate")]
    modification_date: Annotated[str, Field(alias="ModificationDate")]
    online: Annotated[bool, Field(alias="Online")]
    eviction_date: Annotated[str, Field(alias="EvictionDate")]
    s3_path: Annotated[str, Field(alias="S3Path")]
    checksum: Annotated[list[ODataChecksum], Field(alias="Checksum")]
    footprint: Annotated[Geometry | None, Field(alias="Footprint")]
    geo_footprint: Annotated[Geometry | None, Field(alias="GeoFootprint")]


class ODataResult(BaseModel):
    odata_context: Annotated[str, Field(alias="@odata.context")]
    value: list[ODataProduct]
    odata_nextlink: Annotated[str, Field(alias="@odata.nextLink")]


class ODataQuery:
    def __init__(
        self,
        collection: str | None = None,
        name: str | None = None,
        top: int = 20,
        publication_date: tuple[datetime, datetime] | None = None,
        sensing_date: tuple[datetime, datetime] | None = None,
        intersect_geometry: Geometry | None = None,
    ):
        self.collection = collection
        self.name = name
        self.top = top
        self.publication_date = publication_date
        self.sensing_date = sensing_date
        self.intersect_geometry = intersect_geometry

    def to_params(self) -> dict:
        query = []
        if self.collection:
            query.append(f"Collection/Name eq '{self.collection}'")
        if self.name:
            query.append("Name eq '{self.name}'")
        if self.publication_date:
            query.append(
                f"PublicationDate ge {self.publication_date[0].isoformat()} and PublicationDate le {self.publication_date[1].isoformat()}"
            )
        if self.sensing_date:
            query.append(
                f"ContentDate/Start ge {self.sensing_date[0].isoformat()} and ContentDate/Start le {self.sensing_date[1].isoformat()}"
            )
        if self.intersect_geometry:
            query.append(
                f"OData.CSC.Intersects(area=geography'SRID=4326;{self.intersect_geometry.wkt})"
            )

        return {
            "$filter": " and ".join(query),
            "$top": self.top,
        }


class ODataClient:
    def __init__(self, url: str):
        self.url = url

    def search(self, query: ODataQuery) -> Iterator[ODataProduct]:
        response = httpx.get(self.url, params=query.to_params())

        product_collection = ODataResult.model_validate(response.json())
        yield from product_collection.value
