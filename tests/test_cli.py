from eodm.__main__ import app
from typer.testing import CliRunner

runner = CliRunner()


def test_extract_stacapi_items(mock_stac_items):
    result = runner.invoke(app, ["extract", "stac-api", "items", "sample", "sample"])
    assert result.exit_code == 0
    assert "Feature" in result.stdout


def test_extract_stacapi_collections(mock_stac_collections):
    result = runner.invoke(
        app,
        ["extract", "stac-api", "collections", "sample"],
    )
    assert result.exit_code == 0
    assert "Collection" in result.stdout
