import requests
import json
import os
from get_ids import get_ids


def get_json_plant_details() -> None:
    """Retrieves JSON data from the Perenual plant details API and saves it to a json file."""

    url_template = "https://perenual.com/api/species/details/{}?key=sk-JONz674589ab578437782"
    ids = get_ids()

    try:
        # Load existing data from the file
        file_path_details = os.path.join('project', 'database', 'plant_details.json')
        with open(file_path_details, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Iterate over all the ids from get_ids and append the json response to existing data
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
    file_path_json = os.path.join('project', 'database', 'plant_details.json')
    with open(file_path_json, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("All ids saved to plant_details.json")

if __name__ == '__main__':
    get_json_plant_details()