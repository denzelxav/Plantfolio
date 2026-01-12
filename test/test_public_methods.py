import datetime

import pytest
import requests
from PySide6.QtGui import QPixmap

from project.classes.plant import time_average
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency, wiki_page
from project.classes.enums import Sunlight
import images_rc
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency, sunlight_to_string, get_sun_icon_path, string_to_health
from project.classes.enums import Sunlight, Health

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
    assert string_to_sunlight(Sunlight.PART_SUN) == Sunlight.PART_SUN
    assert string_to_sunlight(Sunlight.PART_SHADE) == Sunlight.PART_SHADE
    assert string_to_sunlight(Sunlight.FULL_SHADE) == Sunlight.FULL_SHADE
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
    assert string_to_water_frequency(datetime.timedelta(days=4)) == datetime.timedelta(days=4)
    assert string_to_water_frequency(datetime.timedelta(weeks=1)) == datetime.timedelta(weeks=1)
    assert string_to_water_frequency(datetime.timedelta(weeks=2)) == datetime.timedelta(weeks=2)
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
    expected = {
 'image': 'https://upload.wikimedia.org/wikipedia/commons/4/48/Male_and_female_Cretan_ibex.jpg',
 'title': '<a href="https://en.wikipedia.org/wiki/Kri-kri"><span style=" '
          'text-decoration: underline; color:#00007f;">Kri-kri</span></a>',
 'result': 'success'
                }
    try:
        res = wiki_page("kri-kri", test_mode = True)
        assert all(res[key] == value for key, value in expected.items()) and "description" in res\
            , "Wrong wiki result with internet connection, Feral Goat"
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pass
    except Exception as e:
        raise e

    expected =    {
       'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4f/DandelionFlower.jpg',
       'result': 'success',
       'title': '<a href="https://en.wikipedia.org/wiki/Taraxacum"><span style=" '
       'text-decoration: underline; color:#00007f;">Taraxacum</span></a>'}
    try:
        res = wiki_page("Taraxacum", test_mode=True)
        print(res)
        assert all(res[key]==value for key, value in expected.items()) and "description" in res,\
            "Wrong wiki result with internet connection, Dandelion"
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pass
    except Exception as e:
        raise e

    expected = {'description': 'Species of tree',
              'image': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Ch%C3%A2teau_de_Chenonceau_-_jardin_Russell-Page_%2801%29.jpg',
              'result': 'success',
              'title': '<a href="https://en.wikipedia.org/wiki/Salix_babylonica"><span '
                       'style=" text-decoration: underline; color:#00007f;">Salix '
                       'babylonica</span></a>'}
    try:
        res = wiki_page("Salix babylonica", test_mode=True)
        assert res == expected, "Wrong wiki result with internet connection, weeping willow"
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pass
    except Exception as e:
        raise e

def test_sunlight_to_string():
    """
    Tests all outcomes of sunlight_to_string()
    """
    assert sunlight_to_string(Sunlight.FULL_SHADE) == "full shade"
    assert sunlight_to_string(Sunlight.PART_SUN) == "part sun/part shade"
    assert sunlight_to_string(Sunlight.PART_SHADE) == "part shade"
    assert sunlight_to_string(Sunlight.FULL_SUN) == "full sun"
    with pytest.raises(ValueError) as excinfo:
        sunlight_to_string("This is not a Sunlight enum")
    assert str(excinfo.value) == "Unexpected sunlight value This is not a Sunlight enum"

def test_get_sun_icon_path():
    """
    Tests get_sun_icon_path()
    """
    assert get_sun_icon_path(Sunlight.FULL_SHADE) == ":/full_shade.png"
    assert get_sun_icon_path(Sunlight.PART_SUN) == ":/half_sun.png"
    assert get_sun_icon_path(Sunlight.PART_SHADE) == ":/half_shade.png"
    assert get_sun_icon_path(Sunlight.FULL_SUN) == ":/full_sun.png"
    with pytest.raises(ValueError) as excinfo:
        get_sun_icon_path("This is not a Sunlight enum")
    assert str(excinfo.value) == "Unexpected sunlight value This is not a Sunlight enum"

def test_string_to_health():
    """
    Tests string_to_health()
    """
    assert string_to_health("healthy") == Health.HEALTHY
    assert string_to_health("slightly_unhealthy") == Health.SLIGHTLY_UNHEALTHY
    assert string_to_health("slightly unhealthy") == Health.SLIGHTLY_UNHEALTHY
    assert string_to_health("unhealthy") == Health.UNHEALTHY
    assert string_to_health("dead") == Health.DEAD
    with pytest.raises(ValueError) as excinfo:
        string_to_health("This is not a Health enum")
    assert str(excinfo.value) == "Unexpected health value this is not a health enum"
