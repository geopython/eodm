from eodm.__main__ import app
from typer.testing import CliRunner

runner = CliRunner()


def test_extract_stacapi_items(mock_extract_stac_items):
    result = runner.invoke(app, ["extract", "stac-api", "items", "sample", "sample"])
    assert result.exit_code == 0
    assert "Feature" in result.stdout


def test_extract_stacapi_collections(mock_extract_stac_collections):
    result = runner.invoke(
        app,
        ["extract", "stac-api", "collections", "sample"],
    )
    assert result.exit_code == 0
    assert "Collection" in result.stdout


def test_load_stacapi_items(stac_items, mock_post_stac_api_items_endpoint):
    result = runner.invoke(
        app,
        [
            "load",
            "stac-api",
            "items",
            "https://example.com/stac-api",
            stac_items,
        ],
    )
    assert mock_post_stac_api_items_endpoint.called
    assert result.exit_code == 0
    assert "Feature" in result.stdout


def test_load_stacapi_collections(
    stac_collections, mock_post_stac_api_collections_endpoint
):
    result = runner.invoke(
        app,
        [
            "load",
            "stac-api",
            "collections",
            "https://example.com/stac-api",
            stac_collections,
        ],
    )
    assert mock_post_stac_api_collections_endpoint.called
    assert result.exit_code == 0
    assert "Collection" in result.stdout
