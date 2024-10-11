import pkg_resources
import typer
from dotenv import load_dotenv

from .extract import app as extract
from .load import app as load
from .transform import app as transform

CLI_NAME = "eodm"

app = typer.Typer(name=CLI_NAME, no_args_is_help=True)
app.add_typer(extract)
app.add_typer(transform)
app.add_typer(load)
load_dotenv()


@app.command()
def version():
    """
    Prints software version
    """
    version = pkg_resources.get_distribution(CLI_NAME).version
    print(version)


if __name__ == "__main__":
    app()
