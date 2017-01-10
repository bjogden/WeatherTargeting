# WeatherTargeting

This project is a simple proof-of-concept for acquiring current weather
data from [OpenWeatherMap](https://openweathermap.org/) by zip code and writing it to a JSON file.

To run:

1. Get OpenWeatherMap API key (http://openweathermap.org/appid)

2. Install requirements
    - `pip install -r requirements.pip`

3. Run with `python main.py --zipcode [zipcode int]` or `./main.py --zipcode [zipcode int]` (Python 2.7)

4. Check "logs" subdirectory with JSON file
  - NOTE: log file structure is [zip code]_[OpenWeatherMap weather data timestamp].json
