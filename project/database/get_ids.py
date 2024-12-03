import json

def get_ids() -> list:
    """Returns a list of ids of all indoor plants in the database."""
    
    res = []
    with open('indoor_plants.json', 'r') as file:
        data = json.load(file)
        for dict in data:
            for key, value in dict.items():
                if key == 'id':
                    res.append(value)
    return res


if __name__ == '__main__':
    print(get_ids())
        