import json
import os


def get_indoor_ids() -> list:
    """Returns a list of ids of all indoor plants in indoor_plants.json."""

    res = []
    file_path = os.path.join('database', 'indoor_plants.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
        for dict in data:
            for key, value in dict.items():
                if key == 'id':
                    res.append(value)
    return res


if __name__ == '__main__':
    print(get_indoor_ids())
        