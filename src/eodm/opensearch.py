import re
from datetime import datetime
from enum import Enum
from functools import cached_property
from typing import Any, Generic, Iterator, List, Literal, Union

import lxml.etree as ET
from geojson_pydantic import Feature, Point
from geojson_pydantic.base import _GeoJsonBase
from geojson_pydantic.features import Feat, Props
from geojson_pydantic.geometries import Geometry
from httpx import Client, HTTPTransport
from pydantic import UUID5, BaseModel, Field

XML_PARSER = ET.XMLParser(recover=True)
DEFAULT_TRANSPORT = HTTPTransport(retries=3)


class OpenSearchException(Exception):
    pass


class OpenSearchOption(BaseModel):
    value: str


class OpenSearchParameter(BaseModel):
    name: str
    value: str
    title: str | None = None
    pattern: str | None = None
    minInclusive: int | None = None
    maxInclusive: int | None = None
    options: list[OpenSearchOption] | None = None


class OpenSearchUrl(BaseModel):
    template_url: str
    type: str
    parameters: dict[str, OpenSearchParameter]


class OpenSearchMetadata(BaseModel):
    short_name: str | None = None
    description: str | None = None
    contact: str | None = None
    tags: str | None = None
    long_name: str | None = None
    developer: str | None = None
    attribution: str | None = None
    syndication_right: str | None = None
    language: str | None = None
    input_encoding: str | None = None
    output_encoding: str | None = None


class RelType(str, Enum):
    self = "self"
    search = "search"
    next = "next"
    previous = "previous"
    first = "first"


class OpenSearchLinks(BaseModel):
    rel: RelType
    type: str
    title: str
    href: str


class OpenSearchQuery(BaseModel):
    originalFilters: dict[str, str]
    appliedFilters: dict[str, str]
    processingTime: float


class OpenSearchDownloadServices(BaseModel):
    url: str
    size: int
    mimetype: str | None = None


class OpenSearchServices(BaseModel):
    download: OpenSearchDownloadServices


class OpenSearchDescription(BaseModel):
    shortName: str


class OpenSearchLicense(BaseModel):
    licenseId: str
    hasToBeSigned: str
    viewService: str
    signatureQuota: int
    description: OpenSearchDescription
    grantedCountries: str | None = None
    grantedOrganizationCountries: str | None = None
    grantedFlags: str | None = None


class OpenSearchProperties(BaseModel):
    id: UUID5
    exactCount: int
    startIndex: int
    itemsPerPage: int
    links: list[OpenSearchLinks]
    totalResults: int | None = None


# embarassing that this is needed really
class OpenSearchEmptyCentroid(BaseModel):
    type: None = None
    coordinates: None = None


# properties may vary across implementations, this is creodias specific
class OpenSearchFeatureProperties(BaseModel):
    collection: str
    status: str
    license: OpenSearchLicense
    title: str
    startDate: datetime
    completionDate: datetime
    productType: str
    platform: str
    resolution: float | int
    orbitNumber: int
    updated: datetime
    published: datetime
    services: OpenSearchServices
    links: list[OpenSearchLinks]
    description: str | None = None
    centroid: Point | OpenSearchEmptyCentroid
    instrument: str | None = None
    phase: int | None = None
    organisationName: str | None = None
    processingLevel: str | None = None
    sensorMode: str | None = None
    quicklook: str | None = None
    thumbnail: str | None = None
    snowCover: int | None = None
    cloudClover: int | None = None
    gmlgeometry: str | None = None
    parentIdentifier: str | None = None
    cycle: int | None = None
    productIdentifier: str | None = None
    orbitDirection: str | None = None
    timeliness: str | None = None
    relativeOrbitNumber: int | None = None
    processingBaseline: int | float | None = None


# opensearch artifact, this couln't just be imported from geojson_pydantic
# because opensearch returns a nonstandard properties field **shudders
class FeatureCollection(_GeoJsonBase, Generic[Feat, Props]):
    """
    FeatureCollection Model for creodias OpenSearch, that are extended with nonstandard
    `properties`
    """

    type: Literal["FeatureCollection"]
    features: List[Feat]
    properties: Union[Props] = Field(...)

    def __iter__(self) -> Iterator[Feat]:  # type: ignore [override]
        """iterate over features"""
        return iter(self.features)

    def __len__(self) -> int:
        """return features length"""
        return len(self.features)

    def __getitem__(self, index: int) -> Feat:
        """get feature at a given index"""
        return self.features[index]


OpenSearchFeatureType = Feature[Geometry, OpenSearchFeatureProperties]


# I've no idea how this works
class OpenSearchFeature(OpenSearchFeatureType):
    def to_dict(self) -> dict:
        """Converts to a dictionary"""
        return self.model_dump()


OpenSearchResults = FeatureCollection[OpenSearchFeature, OpenSearchProperties]


class OpenSearchClient:
    NS = {
        "": "http://www.w3.org/2005/Atom",
        "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
        "parameters": "http://a9.com/-/spec/opensearch/extensions/parameters/1.0/",
        "georss": "http://www.georss.org/georss/",
        "media": "http://search.yahoo.com/mrss/",
        "owc": "http://www.opengis.net/owc/1.0/",
        "eo": "http://a9.com/-/opensearch/extensions/eo/1.0/",
        "geo": "http://a9.com/-/opensearch/extensions/geo/1.0/",
        "time": "http://a9.com/-/opensearch/extensions/time/1.0/",
        "cql": "http://a9.com/-/opensearch/extensions/cql/1.0/",
        "dc": "http://purl.org/dc/elements/1.1/",
    }

    def __init__(self, describe_url: str) -> None:
        self.describe_url = describe_url

    def search(
        self,
        query: dict[str, Any],
        mimetype: str = "application/json",
    ) -> Iterator[OpenSearchFeature]:
        """Search for features in the OpenSearch service.

        Args:
            query (dict[str, Any]): Query parameters to search for.
                The keys should match the parameter names in the OpenSearch service and
                have the format `{namespace}:{parameterName}`.
                Example: {"eo:cloudCover": 10}
            mimetype (str, optional): Mimetype.

        Yields:
            Iterator[OpenSearchFeature]: Iterator of OpenSearchFeature object
        """
        search_url = self._prepare_search_url(mimetype, query)
        next_page = True

        while next_page:
            with Client(transport=DEFAULT_TRANSPORT) as client:
                response = client.get(search_url)
                response.raise_for_status()

            # here branch logic for different mimetypes, only json so far known
            feature_collection = OpenSearchResults.model_validate(response.json())

            yield from feature_collection.features

            next_page, url = self._get_next_page(feature_collection.properties.links)

    @cached_property
    def metadata(self) -> OpenSearchMetadata:
        """Service level metadata"""
        data = self._get_raw_describe_data()
        return OpenSearchMetadata(
            short_name=data.findtext("opensearch:ShortName", namespaces=self.NS),
            description=data.findtext("opensearch:Description", namespaces=self.NS),
            contact=data.findtext("opensearch:Contact", namespaces=self.NS),
            tags=data.findtext("opensearch:Tags", namespaces=self.NS),
            long_name=data.findtext("opensearch:LongName", namespaces=self.NS),
            developer=data.findtext("opensearch:Developer", namespaces=self.NS),
            attribution=data.findtext("opensearch:Attribution", namespaces=self.NS),
            syndication_right=data.findtext(
                "opensearch:SyndicationRight", namespaces=self.NS
            ),
            language=data.findtext("opensearch:Language", namespaces=self.NS),
            input_encoding=data.findtext("opensearch:InputEncoding", namespaces=self.NS),
            output_encoding=data.findtext(
                "opensearch:OutputEncoding", namespaces=self.NS
            ),
        )

    @cached_property
    def query_urls(self) -> list[OpenSearchUrl]:
        """List of OpenSearchUrl query objects. Can be used for constructing a query"""
        data = self._get_raw_describe_data()
        query_urls = []
        try:
            for url in data.findall("opensearch:Url", self.NS):
                parameters = {}
                for parameter in url.findall("parameters:Parameter", self.NS):
                    options = []
                    for option in parameter.findall("parameters:Option", self.NS):
                        options.append(OpenSearchOption(value=option.attrib["value"]))

                    min_inclusive = parameter.get("minInclusive")
                    max_inclusive = parameter.get("maxInclusive")
                    parameters[parameter.attrib["value"]] = OpenSearchParameter(
                        name=parameter.attrib["name"],
                        value=parameter.attrib["value"],
                        title=parameter.get("title"),
                        pattern=parameter.get("pattern"),
                        minInclusive=int(min_inclusive) if min_inclusive else None,
                        maxInclusive=int(max_inclusive) if max_inclusive else None,
                        options=options,
                    )

                # another opensearch weirdo, the standard is so non standard
                # that the parameters don't match the template in creodias tsk tsk tsk
                template_url = url.attrib["template"]
                if "uid" in template_url and "uuid" not in template_url:
                    template_url = template_url.replace("uid", "uuid")

                query_urls.append(
                    OpenSearchUrl(
                        template_url=template_url,
                        type=url.attrib["type"],
                        parameters=parameters,
                    )
                )
        except KeyError as e:
            raise OpenSearchException(
                f"Standard attribute '{e.args[0]}' not found"
            ) from e

        return query_urls

    @staticmethod
    def _get_next_page(links: list[OpenSearchLinks]) -> tuple[bool, str]:
        for link in links:
            if link.rel == RelType.next:
                return True, link.href

        return False, ""

    def _get_raw_describe_data(self) -> ET._Element:
        with Client(transport=DEFAULT_TRANSPORT) as client:
            response = client.get(self.describe_url)

        return ET.fromstring(response.content, XML_PARSER)

    def _prepare_search_url(self, mimetype: str, query: dict[str, Any]) -> str:
        for query_url in self.query_urls:
            if query_url.type == mimetype:
                template_url = self._pythonize_template_url(query_url.template_url)

                for k, v in query.items():
                    try:
                        parameter = query_url.parameters[k]
                    except KeyError:
                        raise OpenSearchException(f"Invalid query parameter: {k}")

                    self._validate_query_parameter(v, parameter)

                search_url = self._format_search_url(
                    template_url, query_url.parameters, query
                )
                return search_url

        raise OpenSearchException(f"Couldnt find query url with mimetype: {mimetype}")

    @staticmethod
    def _format_search_url(
        template_url: str,
        query_parameters: dict[str, OpenSearchParameter],
        query: dict[str, Any],
    ) -> str:
        template_query = {}
        for parameter_value, parameter in query_parameters.items():
            template_key = parameter_value.strip("{}").replace(":", "_")
            if template_value := query.get(parameter_value):
                template_query[template_key] = template_value
            else:
                template_query[template_key] = ""

        filled_url = template_url.format(**template_query)

        endpoint, url_parameters = filled_url.split("?")

        final_parameters = []
        for param in url_parameters.split("&"):
            if re.match(".*=.+", param):
                final_parameters.append(param)

        return endpoint + "?" + "&".join(final_parameters)

    @staticmethod
    def _validate_query_parameter(value: Any, parameter: OpenSearchParameter) -> None:
        if parameter.pattern and not re.match(parameter.pattern, value):
            raise OpenSearchException(
                f"{value} not matching regex pattern: {parameter.pattern}"
            )

        if parameter.maxInclusive and value > parameter.maxInclusive:
            raise OpenSearchException(
                f"{value} greater than maxInclusive: {parameter.maxInclusive}"
            )

        if parameter.minInclusive and value < parameter.minInclusive:
            raise OpenSearchException(
                f"{value} less than minInclusive: {parameter.minInclusive}"
            )

        if parameter.options and OpenSearchOption(value=value) not in parameter.options:
            raise OpenSearchException(f"{value} not one of options: {parameter.options}")

    @staticmethod
    def _pythonize_template_url(opensearch_template_url: str) -> str:
        """Converts a template url from the template grammar in
        https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md#template-grammar

        Args:
            opensearch_template_url (str): template URL following abnf rules in RFC2234.
            Example http://test.com?param={ns:paramValue?}

        Returns:
            str: pythonic template url. Example http://test.com?param={ns_paramValue}
        """

        # the first instances of chars below ? and : are ignored because https: and ?
        # for the query parameter

        split_char = "?"
        split_url = opensearch_template_url.split(split_char)
        joined_colon_url = split_url[0] + split_char + "".join(split_url[1:])
        split_char = ":"
        split_url = joined_colon_url.split(split_char)
        pythonic_template_url = split_url[0] + split_char + "_".join(split_url[1:])
        return pythonic_template_url.replace(";", "&")
