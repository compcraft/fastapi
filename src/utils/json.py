import json
from json.decoder import JSONDecodeError
from json.encoder import JSONEncoder


def read_file(path):
    with open(path, 'r') as stream:
        file = json.load(stream)
        return file


def write_file(path, data):
    with open(path, 'w') as fp:
        try:
            json.dump(data, fp)
        except JSONDecodeError as exc:
            print(exc)
