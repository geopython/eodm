from typing import Iterable, Protocol

from eodm.serializers import default_serializer, json_serializer

from ._types import Output


class Mappable(Protocol):
    def to_dict(self): ...


def serialize(data: Iterable[Mappable], output_type: Output) -> None:
    match output_type:
        case Output.json:
            print(json_serializer(data))
        case _:
            for d in default_serializer(data):
                print(d)
