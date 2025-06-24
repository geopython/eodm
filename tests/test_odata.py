from datetime import datetime

from eodm.extract import extract_odata_products
from eodm.odata import ODataCollection, ODataProduct


def test_extract_odata_products(mock_odata_search):
    url = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"
    collections = [ODataCollection.SENTINEL_2]
    datetime_range = (datetime(2020, 1, 1), datetime(2020, 1, 20))
    name_contains = "L2A"
    name_not_contains = "_N9999"
    cloud_cover_less_than = 50

    products = list(
        extract_odata_products(
            url=url,
            collections=collections,
            datetime=datetime_range,
            name_contains=name_contains,
            name_not_contains=name_not_contains,
            cloud_cover_less_than=cloud_cover_less_than,
        )
    )

    assert len(products) == 20
    assert all(isinstance(product, ODataProduct) for product in products)
    assert all(product.name for product in products)
