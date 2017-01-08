__author__ = 'Bryce Ogden'

from datetime import datetime as dt

class Temp(object):
    @staticmethod
    def kelvin_to_cels(num):
        return num - (273.15)

    @staticmethod
    def cels_to_fahr(num):
        return (num * 9/5.0) + 32

    @staticmethod
    def kelvin_to_fahr(num):
        return (num * 9/5.0) - (459.67)

    @staticmethod
    def fahr_to_cels(num):
        return (num - 32) * (5/9.0)

    @staticmethod
    def fahr_to_kelvin(num):
        return (num + 459.67) * (5/9.0)

    @staticmethod
    def cels_to_kelvin(num):
        return num + (273.15)

class Wind(object):
    @staticmethod
    def ms_to_mph(num):
        """ Convert meters/sec. to miles per hour """
        return num / (0.44704)

    @staticmethod
    def mph_to_ms(num):
        return num * (0.44704)

class Date(object):
    @staticmethod
    def timestamp_to_date(stamp):
        return dt.fromtimestamp(stamp).strftime('%Y-%m-%d %H:%M:%S')

class Weather(object):
    """
    List of potential weather "main" values
        (from: https://openweathermap.org/weather-conditions)
    2xx: Thunderstorm
    3xx: Drizzle
    5xx: Rain (rain and drizzle will be the same)
    6xx: Snow
    7xx: Atmosphere
    800: Clear
    80x: Clouds
    90x: Extreme (find exclamation point)
    9xx: Additional (calm, breeze, wind, storm... etc.)
    """
