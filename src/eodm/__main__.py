import importlib
import importlib.metadata
import json
import logging
import sys
from datetime import datetime

import typer
from dotenv import load_dotenv
from pythonjsonlogger.json import JsonFormatter

from .cli.extract import app as extract
from .cli.load import app as load
from .cli.transform import app as transform

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

discovered_plugins = entry_points(group="eodm.plugins")
CLI_NAME = "eodm"

app = typer.Typer(name=CLI_NAME, no_args_is_help=True)

try:
    extract_plugins = discovered_plugins["extract"].load()
    extract.add_typer(extract_plugins)
except KeyError:
    pass
app.add_typer(extract)

try:
    transform_plugins = discovered_plugins["transform"].load()
    transform.add_typer(transform_plugins)
except KeyError:
    pass
app.add_typer(transform)

try:
    load_plugins = discovered_plugins["load"].load()
    load.add_typer(load_plugins)
except KeyError:
    pass
app.add_typer(load)


class EODMFormatter(JsonFormatter):
    EXTRA_PREFIX = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        # update the timestamp format
        log_record["timestamp"] = datetime.now().isoformat()
        log_record["level"] = record.levelname
        log_record["logger_name"] = record.name

        self.set_extra_keys(record, log_record, self._skip_fields)

    @staticmethod
    def is_private_key(key):
        return hasattr(key, "startswith") and key.startswith("_")

    @staticmethod
    def is_extra_key(key):
        return hasattr(key, "startswith") and key.startswith(EODMFormatter.EXTRA_PREFIX)

    @staticmethod
    def set_extra_keys(record, log_record, reserved):
        """
        Add the extra data to the log record.
        prefix will be added to all custom tags.
        """
        record_items = list(record.__dict__.items())
        records_filtered_reserved = [
            item for item in record_items if item[0] not in reserved
        ]
        records_filtered_private_attr = [
            item
            for item in records_filtered_reserved
            if not EODMFormatter.is_private_key(item[0])
        ]

        for key, value in records_filtered_private_attr:
            if not EODMFormatter.is_extra_key(key):
                if isinstance(value, (dict, list)):
                    value = json.dumps(value)
                new_key_name = f"{EODMFormatter.EXTRA_PREFIX}{key}"
                log_record[new_key_name] = value
                log_record.pop(key, None)


@app.callback()
def main(
    with_env: bool = False,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """
    Create batch ETL of Earth Observation data for various sources and targets.
    """
    if with_env:
        load_dotenv()

    lvl = logging.INFO
    if verbose:
        lvl = logging.DEBUG

    log_handler = logging.StreamHandler()
    formatter = EODMFormatter()
    log_handler.setFormatter(formatter)
    logging.basicConfig(level=lvl, handlers=[log_handler])


@app.command()
def version():
    """
    Prints software version
    """
    version = importlib.metadata.version("eodm")
    print(version)


if __name__ == "__main__":
    app()
