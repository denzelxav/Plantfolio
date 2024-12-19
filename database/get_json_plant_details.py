import json
import os
import requests
from database.get_ids import get_ids


def get_json_plant_details() -> None:
    """
    Retrieve all the plant details from the API and save them to a JSON file
    """
    url_template = "https://perenual.com/api/species/details/{}?key=sk-JONz674589ab578437782"
    ids = get_ids()

    try:
        file_path = os.path.join('database', 'plant_details.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    for plant_id in ids:
        url = url_template.format(plant_id)
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            existing_data.append(data)
            print(f"Retrieved plant_id: {plant_id}")
        else:
            print(f"Failed to retrieve plant_id: {plant_id}")
            break

    # Save all the JSON responses to a file
    with open('plant_details.json', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4)

    print("All ids saved to plant_details.json")
