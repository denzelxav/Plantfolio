"""
This module contains independent public methods
"""

from __future__ import annotations
import datetime


import urllib.request as urllib
import json
import requests
from PySide6.QtGui import QPixmap
from project.classes.enums import Sunlight, Health



def wiki_page(plant: str, test_mode=False) -> dict[str, str | QPixmap]:
    """
    Searches plants scientific name on wikipedia.
    Returns dictionary with hyperlink, description and high-res thumbnail
    """
    language_code = 'en'
    split_plant = plant.split(' ')
    i = 2 if len(split_plant) > 1 else 1
    search_query = " ".join(split_plant[:i])
    number_of_results = 1
    key = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzYjA4Y"
           "mYwMThhMTMwYTM5YTBiNDVlMGU2MmIwYjRkYyIsImp0aSI6IjY4YTQ"
           "4MmE0ZGEyMGQ4MjU0OGI5ZjdlNzJlNTgyYzMxNjE1Y2JiNjRkOWVjM"
           "DQ4MjYyMTM5MDYzYjcxZDYzNmUwNDA5NDMxZjdhNWEyOWMxIiwiaWF"
           "0IjoxNzM2ODUxMTIzLjg4OTYzMywibmJmIjoxNzM2ODUxMTIzLjg4O"
           "TYzNywiZXhwIjozMzI5Mzc1OTkyMy44ODY5MSwic3ViIjoiNzczOTE"
           "xOTIiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsI"
           "nJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5"
           "pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIl19.PO98S2HQDYjD"
           "ZyZCGE_fcbcqjtx-bEi681mCJsRk2uCzmEVkV1qAmiWArZtGtErus4"
           "VVxuHG9pwdGsSIgGcKNfSl3V55Y1BveA1iIl5wTZfiBnmg6V5trFCG"
           "h6M7_volAIW-NN-wtU0oBbgNzwkzTUH5W7ZEvZ0vb-5DqUIjggpllL"
           "_ze5xdfe738KdJbMK0jc3R_J1GD8eQnmVUDmeKtDJVgeMVpIoa9x4_"
           "ABuMhUlTGkPqJ1cpylMm8Mk4dCC6oGtQKwwed3BjzU8WZIbpwNT8tA"
           "szLOPaRg9o5kfclSdtfVc6sMxiEj6Ide-fVV_vpHR1rVfasfoG3CxT"
           "gGa-6I8aY_1JzJMUOxflYp-NsVoRlc_CoFmC5y2ez8pOdn1d_Jd5TR"
           "v1BDl_jH3F0xmLaVADe7U1XPqDPMiv7dzl0ziwLaTxECYeh-eqrwKj"
           "Tk8vRmMhbSQyR_6N2PFktURJsF2VW3rVRwtfLH1KaXxQz5i3P1btpl"
           "2ktijSzug-3LRI6xdo-JkkHsfmZGPSQBW5hqIGj2IXuwT1zfk_nrhZ"
           "nk--G1Btsm4IOwVMHKQHj8JBJ6FLDkY0Buqs6lqZ-6ZW6b39yPNx-S"
           "tdLmf3Fi0q2oQ56SIBvJVGD_hoJkVMGcXRPzHNn0VAvC1dSQ1CxdCZ"
           "BX8TeT9mtvDiSwC4_fbQwDQ")
    headers = {
        'Authorization': key,
        'User-Agent': 'Plantfolio (denzeltraeger@hotmail.com)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response_code = requests.get(url, headers=headers, params=parameters, timeout=5) # type: ignore
    response = json.loads(response_code.text)
    if (response_code.status_code != 200 or
            len(response["pages"]) == 0 or
            plant.split(" ")[0].lower() not in response["pages"][0]["title"].lower()):
        if not test_mode:
            pixmap = QPixmap(":/plant_1_healthy.png")
        else:
            pixmap = "test_image" # type: ignore
        return {"title": "No wiki page available", "description": "...", "image": pixmap}
    page = response["pages"][0]
    display_title = page["title"]
    description = page['description']
    try:
        thumbnail_url = 'https:' + page['thumbnail']['url']
        thumbnail_url = thumbnail_url.replace("/thumb", "")
        i1 = thumbnail_url.rfind('/')
        thumbnail_url = thumbnail_url[:i1]
        if not test_mode:
            with urllib.urlopen(thumbnail_url).read() as data:
                pixmap = QPixmap()
                pixmap.loadFromData(data)
        else:
            pixmap = thumbnail_url
    except TypeError:
        if not test_mode:
            pixmap = QPixmap(":/plant_1_healthy")
        else:
            pixmap = "test_image" # type: ignore
    except Exception as e:
        raise e
    page_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
    return {
        "title": '<a href="' + page_url + '">' +
                 '<span style=" text-decoration: underline; color:#00007f;">' +
                 display_title +
                 "</span>" +
                 '</a>',
        "description": description,
        "image": pixmap
    }


def string_to_sunlight(sunlight_string: str) -> Sunlight:
    """Converts sunlight string from core database to Sunlight enum"""
    if isinstance(sunlight_string, (str, Sunlight)):
        match sunlight_string:
            case "full shade" | "deep shade" | "sun-part shade":
                return Sunlight.FULL_SHADE
            case "part sun" | "part sun/part shade" | " part sun/part shade":
                return Sunlight.PART_SUN
            case "part shade" | "filtered shade":
                return Sunlight.PART_SHADE
            case "full sun" | "full sun only if soil kept moist":
                return Sunlight.FULL_SUN
            case sunlight if isinstance(sunlight, Sunlight):
                return sunlight
            case unexpected_value:
                raise ValueError(f"Unexpected sunlight value {unexpected_value}")
    else:
        raise TypeError(f"Expected str type. Got {type(sunlight_string)}. Value: {sunlight_string}")

def sunlight_to_string(sunlight: Sunlight) -> str:
    """
    Returns string representation of Sunlight enum
    """
    match sunlight:
        case Sunlight.FULL_SHADE:
            return "full shade"
        case Sunlight.PART_SUN:
            return "part sun/part shade"
        case Sunlight.PART_SHADE:
            return "part shade"
        case Sunlight.FULL_SUN:
            return "full sun"
        case unexpected_value:
            raise ValueError(f"Unexpected sunlight value {unexpected_value}")


def string_to_water_frequency(watering_string: str) -> datetime.timedelta:
    """Converts water frequency string from core database to appropriate datetime.timedelta"""
    if isinstance(watering_string, datetime.timedelta):
        return watering_string
    if isinstance(watering_string, str):
        match watering_string.lower():
            case "frequent":
                return datetime.timedelta(days=4)
            case "average":
                return datetime.timedelta(weeks=1)
            case "minimum":
                return datetime.timedelta(weeks=2)
            case unexpected_value:
                raise ValueError(f"Unexpected watering_string {unexpected_value}")
    else:
        raise TypeError(
            f"Expected str type. Got {type(watering_string)}. Value: {watering_string}"
        )

def get_sun_icon_path(sunlight: Sunlight) -> str:
    """
    returns the path to the appropriate sunlight icon
    """
    match sunlight:
        case Sunlight.FULL_SHADE:
            return ":/full_shade.png"
        case Sunlight.PART_SUN:
            return ":/half_sun.png"
        case Sunlight.PART_SHADE:
            return ":/half_shade.png"
        case Sunlight.FULL_SUN:
            return ":/full_sun.png"
        case unexpected_value:
            raise ValueError(f"Unexpected sunlight value {unexpected_value}")

def string_to_health(health: str) -> Health:
    """
    Returns Health enum that corresponds to given string
    """
    match health.lower():
        case "healthy":
            return Health.HEALTHY
        case "slightly unhealthy" | "slightly_unhealthy":
            return Health.SLIGHTLY_UNHEALTHY
        case "unhealthy":
            return Health.UNHEALTHY
        case "dead":
            return Health.DEAD
        case unexpected_value:
            raise ValueError(f"Unexpected health value {unexpected_value}")
