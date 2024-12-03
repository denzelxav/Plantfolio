import requests
import json


def get_json_plant_disseases() -> None:
    """Retrieves JSON data from the Perenual disease API and saves it to a json file."""
    
    url_template = "https://perenual.com/api/pest-disease-list?key=sk-JONz674589ab578437782&page={}"

    try:
        # Load existing data from the file
        with open('plants_disseases.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Iterate over all the pages and append the json response to existing data
    for page in range(1, 9):
        url = url_template.format(id)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            existing_data.append(data)
            print(f"Retrieved id: {page}")
        else:
            print(f"Failed to retrieve id: {page}")
            break

    # Save existing data to a json file
    with open('plants_disseases.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("All pages saved to plant_details.json")

if __name__ == '__main__':
    get_json_plant_disseases()