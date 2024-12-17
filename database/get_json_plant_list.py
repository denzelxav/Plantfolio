import json
import requests


def get_json_plant_list() -> None:
    """
    Retrieve all the indoor plant list from the API and save them to a JSON file
    """
    url_temp = "https://perenual.com/api/species-list?key=sk-fDCj6745885face837780&page={}&indoor=1"
    try:
        with open('indoor_plants.json', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    for page in range(1, 8):
        url = url_temp.format(page)
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            existing_data.extend(data['data'])
            print(f"Retrieved page {page}")
        else:
            print(f"Failed to retrieve page {page}")
            break

    # Save all the JSON responses to a file
    with open('indoor_plants.json', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4)

    print("All pages saved to response.json")
