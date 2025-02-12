# Plugins

`eodm` offers an option to add extract, transform or load plugins.
Below is a minimal transform example.

`pyproject.toml`

```toml
[project]
name = "eodm_plugin"
version = "0.0.0"
dependencies = [
    "eodm"
]

[project.entry-points.'eodm.plugins'] # the entry-point group is the `eodm.plugins`
transform = 'plugins:app' # the plugin finds `extract`, `transform` or `load` entry points with the name `app` in the package `plugins`
```

`eodm_plugin/plugins.py`

```python
import typer

app = typer.Typer(name="plugin", no_args_is_help=True)


@app.command()
def test():
    print("This is a plugin")
```

The application gets extended with the group called `plugin` (same as the typer app name)
and a single command `test`:

```shell
eodm transform plugin test
```

This is a sample to get you up to speed. A properly implemented plugin should work by
accepting and outputting STAC items, in order to create a full pipeline and leverage
existing functions around the plugin that work by taking STAC and outputting STAC.

## Docker

In addition to creating the plugin, you may need a custom docker image. In that case simply
extend the existing docker image and install your plugin.

```Dockerfile
FROM ghcr.io/geopython/eodm

WORKDIR /app
COPY . .

RUN pip3 install .
```
