import requests
import json


def get_json_plant_list() -> None:
    """Retrieves JSON data from the Perenual plant list API and saves it to a json file."""

    url_template = "https://perenual.com/api/species-list?key=sk-fDCj6745885face837780&page={}&indoor=1"
    
    try:
        with open('indoor_plants.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Iterate over all the pages with indoor plants only and append the json response to existing data
    for page in range(1, 8):
        url = url_template.format(page)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            existing_data.extend(data['data'])
            print(f"Retrieved page {page}")
        else:
            print(f"Failed to retrieve page {page}")
            break

    # Save all the JSON responses to a file
    with open('indoor_plants.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("All pages saved to response.json")


if __name__ == '__main__': 
    get_json_plant_list()
