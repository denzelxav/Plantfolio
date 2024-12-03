import requests
import json
from database.get_ids import get_ids
import os


def get_json_plant_details() -> None:
    url_template = "https://perenual.com/api/species/details/{}?key=sk-JONz674589ab578437782"
    ids = get_ids()

    try:
        file_path = os.path.join('database', 'plant_details.json')
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    for id in ids:
        url = url_template.format(id)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            existing_data.append(data)
            print(f"Retrieved id: {id}")
        else:
            print(f"Failed to retrieve id: {id}")
            break

    # Save all the JSON responses to a file
    with open('plant_details.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("All ids saved to plant_details.json")

if __name__ == '__main__':
    get_json_plant_details()