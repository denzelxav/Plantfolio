import json
import os


def get_ids() -> list:
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
    print(get_ids())
        