import json
from typing import Callable, Iterable, Protocol

from eodm.cli._types import Output


class Mappable(Protocol):
    def to_dict(self): ...


def default_item_encoder(items: Iterable[Mappable]) -> None:
    for item in items:
        print(json.dumps(item.to_dict()))


def json_item_encoder(items: Iterable[Mappable]) -> None:
    print(json.dumps([item.to_dict() for item in items]))


OUTPUT_ENCODERS: dict[Output, Callable[[Iterable[Mappable]], None]] = {
    Output.default: default_item_encoder,
    Output.json: json_item_encoder,
}
