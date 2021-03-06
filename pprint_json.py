import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as any_json:
        in_json = json.load(any_json)
    return in_json


def json_format(json_data):
    return json.dumps(json_data, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    in_json = load_data(sys.argv[1])
    out_json = json_format(in_json)
    print (out_json)
