from typing import Any

import fsspec
from pystac import StacIO
from pystac.utils import HREF


class FSSpecStacIO(StacIO):
    """
    Extension of StacIO to allow working with different filesystems in STAC using fsspec.

    More information: https://pystac.readthedocs.io/en/stable/concepts.html#i-o-in-pystac
    """

    def __init__(
        self,
        headers: dict[str, str] | None = None,
        filesystem: fsspec.AbstractFileSystem | None = None,
    ) -> None:
        self.filesystem = filesystem
        super().__init__(headers=headers)

    def write_text(self, dest: HREF, txt: str, *args: Any, **kwargs: Any) -> None:
        if self.filesystem:
            with self.filesystem.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)
        else:
            with fsspec.open(dest, "w", *args, **kwargs) as f:
                f.write(txt)

    def read_text(self, source: HREF, *args: Any, **kwargs: Any) -> str:
        if self.filesystem:
            with self.filesystem.open(source, "r", *args, **kwargs) as f:
                return f.read()
        else:
            with fsspec.open(source, "r", *args, **kwargs) as f:
                return f.read()
