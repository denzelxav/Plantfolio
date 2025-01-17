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
          'text-decoration: underline; color:#00007f;">Kri-kri</span></a>',
 'result': 'success'
                }
    try:
        res = wiki_page("kri-kri", test_mode = True)
        assert res == expected, "Wrong wiki result with internet connection, Feral Goat"
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pass
    except Exception as e:
        raise e

    expected =    {
       'description': 'Genus of flowering plants in the daisy family Asteraceae',
       'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4f/DandelionFlower.jpg',
       'result': 'success',
       'title': '<a href="https://en.wikipedia.org/wiki/Taraxacum"><span style=" '
       'text-decoration: underline; color:#00007f;">Taraxacum</span></a>'}
    try:
        res = wiki_page("Taraxacum", test_mode=True)
        assert res == expected, "Wrong wiki result with internet connection, Dandelion"
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