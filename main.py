#!/usr/bin/env python2
__author__ = 'Bryce Ogden'

import requests
import json
import os
import config

from utils import Temp, Wind, Date

zip_code = '90245' # El Segundo
zip_code = '89158' # Aria, Las Vegas

def get_weather(zip_code):
    """ Grab weather data from OpenWeatherMap """

    url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}'.format(zip_code, config.KEY)

    r = requests.get(url)

    if r.status_code == 200:
        parse_weather(r.text)
    else:
        print('OpenWeatherMap status code: {}'.format(r.status_code))


def parse_weather(data):
    """ Parse weather data from get_weather """

    weather_data = json.loads(data)

    # DATE UPDATED
    date = weather_data.get('dt', 0)

    # LOCATION
    city = weather_data.get('name', 'null').encode('utf8')
    lat = weather_data.get('coord', {}).get('lat', 0)
    lon = weather_data.get('coord', {}).get('lon', 0)

    # TEMPERATURE
    # Current temp
    temp = weather_data.get('main', {}).get('temp', 'N/A')
    if temp != 'N/A':
        temp = Temp.kelvin_to_fahr(temp)

    # High temp
    high_temp = weather_data.get('main', {}).get('temp_max', 'N/A')
    if high_temp != 'N/A':
        high_temp = Temp.kelvin_to_fahr(high_temp)

    # Low temp
    low_temp = weather_data.get('main', {}).get('temp_min', 'N/A')
    if low_temp != 'N/A':
        low_temp = Temp.kelvin_to_fahr(low_temp)

    # Humidity (percentage)
    humidity = weather_data.get('main', {}).get('humidity', 0) / 100.0

    # WEATHER CONDITIONS (e.g. "clouds")
    conditions = weather_data.get('weather', None)
    if conditions:
        conditions = str(conditions[0].get('main', '')).lower()
        # Changing "additional" to "windy"
        if conditions == "additional":
            conditions = "windy"

    # WIND SPEED
    wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
    if wind_speed:
        wind_speed = Wind.ms_to_mph(wind_speed)

    # TIME OF DAY
    sunrise = weather_data.get('sys', {}).get('sunrise', 'N/A')
    sunset = weather_data.get('sys', {}).get('sunset', 'N/A')

    print(Date.timestamp_to_date(date), city, lat, lon, temp, high_temp,
        low_temp, humidity, conditions,
        wind_speed, Date.timestamp_to_date(sunrise), Date.timestamp_to_date(sunset)
    )

    data = {
        "day": {
            "date": date,
            "sunrise": sunrise,
            "sunset": sunset
        },
        "location": {
            "city": city,
            "lat": lat,
            "lon": lon
        },
        "temp": {
            "current": int(round(temp)),
            "high": int(round(high_temp)),
            "low": int(round(low_temp)),
            "humidity": humidity,
            "units": "fahrenheit"
        },
        "conditions": conditions,
        "wind": {
            "speed": int(round(wind_speed)),
            "units": "mph"
        }
    }

    fname = '{}_{}.json'.format(zip_code, date)
    write_to_file(fname, data)


def write_to_file(fname, json_data):
    """ Take JSON data and dump into file """

    logs = '{}/{}'.format(os.getcwd(), config.LOG_DIR)
    if not os.path.exists(logs):
        os.makedirs(logs)

    with open('{}/{}'.format(logs, fname), 'w') as f:
        json.dump(json_data, f)


def main():
    get_weather(zip_code)


if __name__ == '__main__':
    main()

