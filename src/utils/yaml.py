import yaml


def read_file(path):
    with open(path, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
            return file
        except yaml.YAMLError as exc:
            print(exc)


def write_file(path, data):
    with open(path, 'w') as fp:
        try:
            fp.write(yaml.dump(data))
        except yaml.YAMLError as exc:
            print(exc)
