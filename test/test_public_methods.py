import datetime

import pytest
import requests
from PySide6.QtGui import QPixmap

from project.classes.plant import time_average
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency, wiki_page
from project.classes.enums import Sunlight
import images_rc

def test_string_to_sunlight():
    """
    Tests all outcomes of string_to_sunlight()
    """
    assert string_to_sunlight('full shade') == Sunlight.FULL_SHADE
    assert string_to_sunlight('deep shade') == Sunlight.FULL_SHADE
    assert string_to_sunlight('part sun/part shade') == Sunlight.PART_SUN
    assert string_to_sunlight('part shade') == Sunlight.PART_SHADE
    assert string_to_sunlight('filtered shade') == Sunlight.PART_SHADE
    assert string_to_sunlight('full sun') == Sunlight.FULL_SUN
    assert string_to_sunlight(Sunlight.FULL_SUN) == Sunlight.FULL_SUN
    with pytest.raises(ValueError) as excinfo:
        string_to_sunlight("Unknown value")
    assert str(excinfo.value) == "Unexpected sunlight value Unknown value"

    with pytest.raises(TypeError) as excinfo:
        string_to_sunlight(5)
    assert str(excinfo.value) == "Expected str type. Got <class 'int'>. Value: 5"

def test_string_to_water_frequency():
    """
    Tests all outcomes of string_to_water_frequency()
    """
    assert string_to_water_frequency("frequent") == datetime.timedelta(days=4)
    assert string_to_water_frequency("average") == datetime.timedelta(weeks=1)
    assert string_to_water_frequency("minimum") == datetime.timedelta(weeks=2)
    assert string_to_water_frequency(datetime.timedelta(days=1)) == datetime.timedelta(days=1)
    with pytest.raises(ValueError) as excinfo:
        string_to_water_frequency("Unknown value")
    assert str(excinfo.value) == "Unexpected watering_string unknown value"
    with pytest.raises(TypeError) as excinfo:
        string_to_water_frequency(1)
    assert str(excinfo.value) == "Expected str type. Got <class 'int'>. Value: 1"

def test_time_average():
    """
    Tests time_average()
    """
    test_list = [datetime.datetime.now() + datetime.timedelta(days = 1) * i for i in range(10)]
    test_average = time_average(test_list)
    assert test_average <= datetime.timedelta(days = 1, seconds=10)

def test_wiki_page():
    expected = {'description': 'Feral goat',
 'image': 'https://upload.wikimedia.org/wikipedia/commons/4/48/Male_and_female_Cretan_ibex.jpg',
 'title': '<a href="https://en.wikipedia.org/wiki/Kri-kri"><span style=" '
          'text-decoration: underline; color:#00007f;">Kri-kri</span></a>'}
    try:
        requests.get("https://www.google.com", timeout=5)
        connected = True
    except (requests.ConnectionError, requests.Timeout):
        # user has no internet
        connected = False
    except Exception as e:
        raise e
    res = wiki_page("kri-kri", test_mode = True)
    if connected:
        assert res == expected, "Wrong wiki result with internet connection"
    if not connected:
        assert res == {"title": "No wiki page available", "description": "...", "image": "test_image"}, \
            "Failed request doesn't return default dictionary"