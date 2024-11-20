import json
from typing import Iterable, Protocol

from eodm.cli._types import Output


class Mappable(Protocol):
    def to_dict(self): ...


def default_serializer(items: Iterable[Mappable]) -> None:
    """Serializes a list of Mappables (containing to_dict()) to json and prints each
    individually

    Args:
        items (Iterable[Mappable]): A collection of Mappable items
    """
    for item in items:
        print(json.dumps(item.to_dict()))


def json_serializer(items: Iterable[Mappable]) -> None:
    """Serializes a list of Mappables (containing to_dict()) to a json list

    Args:
        items (Iterable[Mappable]): A collection of Mappable items
    """
    print(json.dumps([item.to_dict() for item in items]))


def serialize(data: Iterable[Mappable], output_type: Output) -> None:
    match output_type:
        case Output.default:
            default_serializer(data)
        case Output.json:
            json_serializer(data)
        case _:
            default_serializer(data)
