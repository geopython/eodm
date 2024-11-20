from typing import Any

import fsspec
from pystac import HREF, StacIO


class FSSpecStacIO(StacIO):
    """
    Extension of StacIO to allow working with different filesystems in STAC using fsspec.

    More information: https://pystac.readthedocs.io/en/stable/concepts.html#i-o-in-pystac
    """

    def write_text(self, dest: HREF, txt: str, *args: Any, **kwargs: Any) -> None:
        if fs := kwargs.get("filesystem"):
            with fs.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)
        else:
            with fsspec.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)

    def read_text(self, source: HREF, *args: Any, **kwargs: Any) -> str:
        if fs := kwargs.get("filesystem"):
            with fs.open(source, "r", *args, **kwargs) as f:
                return f.read()
        else:
            with fsspec.open(source, "r", *args, **kwargs) as f:
                return f.read()


__all__ = ["FSSpecStacIO"]
