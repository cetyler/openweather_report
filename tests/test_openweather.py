import pytest
from openweather_report.openweather import OpenWeatherMap


def test_api_version():
    owm = OpenWeatherMap()

    assert owm.api_version("2.5") == "http://api.openweathermap.org/data/2.5/"
    assert owm.api_version("3.0") == "http://api.openweathermap.org/data/3.0/"
