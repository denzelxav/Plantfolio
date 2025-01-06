import datetime

import pytest
from project.classes.plant import time_average
from project.classes.public_methods import string_to_sunlight, string_to_water_frequency
from project.classes.enums import Sunlight

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
    assert str(excinfo.value) == "Unexpected watering_string Unknown value"
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
