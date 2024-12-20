import pytest
from data.test_data import OPENSEARCH_PRODUCT_TYPES
from eodm.opensearch import OpenSearchClient


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
