from eodm.extract import extract_ogcapi_records, extract_ogcapi_records_catalogs


def test_extract_ogcapi_records_catalogs():
    url = "https://resource-catalogue.apx.develop.eoepca.org"
    for i in extract_ogcapi_records_catalogs(url):
        assert i["type"] == "catalog"


def test_extract_ogcapi_records():
    url = "https://resource-catalogue.apx.develop.eoepca.org"
    catalog_ids = ["S2MSI1C"]
    datetime_interval = "2018-01-01/2020-01-01"
    bbox = [15.7308, 47.4577, 17.2709, 48.2459]
    for i in extract_ogcapi_records(url, catalog_ids, datetime_interval, bbox):
        assert i["type"] == "Feature"
