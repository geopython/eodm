from typing import Annotated

import typer

from eodm.cli._serialization import serialize
from eodm.cli._types import (
    Output,
    OutputType,
)
from eodm.extract import extract_opensearch_features

app = typer.Typer(no_args_is_help=True, help="Extract features from a OpenSearch API")


@app.command(no_args_is_help=True)
def features(
    url: str,
    product_type: str,
    limit: Annotated[
        int,
        typer.Option(
            "--limit",
            "-l",
            metavar="INT",
            help="Limit number of results",
        ),
    ] = 0,
    output: OutputType = Output.default,
):
    """
    Extract features found in an OpenSearch API given a product type
    """

    features = extract_opensearch_features(
        url=url,
        product_types=[product_type],
        limit=limit,
    )
    serialize(features, output_type=output)  # type: ignore[arg-type]
