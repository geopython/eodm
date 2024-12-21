import pytest
from data.test_data import OPENSEARCH_PRODUCT_TYPES
from eodm.opensearch import OpenSearchClient, OpenSearchException


@pytest.mark.parametrize("opensearch_product_type", OPENSEARCH_PRODUCT_TYPES)
def test_opensearch_search(
    mock_opensearch_describe, mock_opensearch_search, opensearch_product_type
):
    client = OpenSearchClient(
        "https://finder.creodias.eu/resto/api/collections/describe.xml"
    )

    query = {"{count}": 3, "{eo:productType}": opensearch_product_type}
    for i in client.search(query):
        assert i


def test_opensearch_invalid_product_type(mock_opensearch_describe):
    client = OpenSearchClient(
        "https://finder.creodias.eu/resto/api/collections/describe.xml"
    )

    query = {"{count}": 3, "{eo:productType}": "INVALID"}
    with pytest.raises(OpenSearchException):
        for i in client.search(query):
            i


def test_opensearch_invalid_count(mock_opensearch_describe):
    client = OpenSearchClient(
        "https://finder.creodias.eu/resto/api/collections/describe.xml"
    )

    query = {"{count}": -5, "{eo:productType}": OPENSEARCH_PRODUCT_TYPES[0]}
    with pytest.raises(OpenSearchException):
        for i in client.search(query):
            i
