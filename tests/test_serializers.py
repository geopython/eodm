import json

from eodm.serializers import default_serializer, json_serializer


class MappableMock:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {"foo": "bar", "data": self.data}


TEST_DATA = [MappableMock(1), MappableMock(2), MappableMock(3)]


def test_json_serializer(capsys):
    out = json_serializer(TEST_DATA)
    assert (
        out
        == '[{"foo": "bar", "data": 1}, {"foo": "bar", "data": 2}, {"foo": "bar", "data": 3}]'
    )


def test_default_serializer(capsys):
    for out, data in zip(default_serializer(TEST_DATA), TEST_DATA):
        assert out == json.dumps(data.to_dict())
