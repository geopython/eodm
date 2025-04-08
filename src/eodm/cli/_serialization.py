from typing import Iterable, Protocol

from eodm.serializers import default_serializer, id_serializer, json_serializer

from ._types import Output


class Mappable(Protocol):
    def to_dict(self): ...

    @property
    def id(self) -> str: ...


def serialize(data: Iterable[Mappable], output_type: Output) -> None:
    match output_type:
        case Output.json:
            print(json_serializer(data))
        case Output.id:
            for d in id_serializer(data):
                print(d)
        case _:
            for d in default_serializer(data):
                print(d)
