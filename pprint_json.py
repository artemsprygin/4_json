import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as handle:
        raw_json = json.load(handle)
    return raw_json


def pretty_print_json(data):
    return json.dumps(data, indent=4)


if __name__ == '__main__':
    raw_json = load_data(sys.argv[1])
    print(pretty_print_json(raw_json))
