import json
import os


def get_ids() -> list:
    """
    Return a list of all indoor plant ids in the database
    """
    res = []
    file_path = os.path.join('database', 'indoor_plants.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for plant in data:
            for key, value in plant.items():
                if key == 'id':
                    res.append(value)
    return res
