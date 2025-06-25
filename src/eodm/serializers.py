import json
from typing import Iterable, Protocol


class Mappable(Protocol):
    def to_dict(self): ...

    @property
    def id(self) -> str: ...


def id_serializer(items: Iterable[Mappable]) -> Iterable[str]:
    """Serializes a list of Mappables (implementing to_dict()) to a list of ids


    Args:
        items (Iterable[Mappable]): A collection of Mappable items

    Returns:
        Iterable[str]: item as a string

    Yields:
        Iterator[Iterable[str]]: Collection of ids
    """

    for item in items:
        yield item.id


def default_serializer(items: Iterable[Mappable]) -> Iterable[str]:
    """Serializes a list of Mappables (implementing to_dict()) to json strings
    individually


    Args:
        items (Iterable[Mappable]): A collection of Mappable items

    Returns:
        Iterable[str]: item as a string

    Yields:
        Iterator[Iterable[str]]: Collection of json strings
    """

    for item in items:
        yield json.dumps(item.to_dict(), default=str)


def json_serializer(items: Iterable[Mappable]) -> str:
    """Serializes a list of Mappables (implementing to_dict()) to a json list

    Args:
        items (Iterable[Mappable]): A collection of Mappable items

    Returns:
        str: items as a json list
    """
    return json.dumps([item.to_dict() for item in items], default=str)
