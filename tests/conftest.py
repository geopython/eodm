import pytest
from pytest_mock import MockerFixture
from test_data import STAC_COLLECTIONS, STAC_ITEMS


@pytest.fixture()
def mock_stac_collections(mocker: MockerFixture):
    client_mock = mocker.patch("eodm.extract.pystac_client.Client")
    client_mock.open().get_collections().__iter__.return_value = STAC_COLLECTIONS


@pytest.fixture()
def mock_stac_items(mocker: MockerFixture):
    client_mock = mocker.patch("eodm.extract.pystac_client.Client")
    client_mock.open().search().item_collection().__iter__.return_value = STAC_ITEMS
