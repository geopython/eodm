import json
from pathlib import Path

import pytest
import respx
from httpx import Response
from pytest_mock import MockerFixture
from test_data import STAC_COLLECTIONS, STAC_ITEMS


@pytest.fixture()
def mock_extract_stac_collections(mocker: MockerFixture):
    client_mock = mocker.patch("eodm.extract.pystac_client.Client")
    client_mock.open().get_collections().__iter__.return_value = STAC_COLLECTIONS


@pytest.fixture()
def mock_extract_stac_items(mocker: MockerFixture):
    client_mock = mocker.patch("eodm.extract.pystac_client.Client")
    client_mock.open().search().item_collection().__iter__.return_value = STAC_ITEMS


@pytest.fixture()
def stac_collections(tmp_path: Path):
    collection_json_path = tmp_path / "collections"

    with collection_json_path.open("a", encoding="utf-8", newline="\n") as f:
        for collection in STAC_COLLECTIONS:
            f.write(json.dumps(collection.to_dict()))
            f.write("\n")

    return str(collection_json_path)


@pytest.fixture()
def stac_items(tmp_path):
    item_json_path = tmp_path / "items"

    with item_json_path.open("a", encoding="utf-8", newline="\n") as f:
        for item in STAC_ITEMS:
            f.write(json.dumps(item.to_dict()))
            f.write("\n")

    return str(item_json_path)


@pytest.fixture()
def mock_post_stac_api_items_endpoint(respx_mock: respx.MockRouter):
    post_mock = respx_mock.post(
        "https://example.com/stac-api/collections/sentinel-2-l2a/items"
    ).mock(return_value=Response(204))
    return post_mock


@pytest.fixture()
def mock_post_stac_api_collections_endpoint(respx_mock: respx.MockRouter):
    post_mock = respx_mock.post("https://example.com/stac-api/collections").mock(
        return_value=Response(204)
    )
    return post_mock
