import requests
from rich import print_json

geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
weather_url = "https://api.openweathermap.org/data/2.5/forecast"
key = '28d4883cb180676d90561d43c5caa22f'

def get_geo_location(city):
  geo_params = {
    'q': city,
    'appid': key
  }

  response = requests.get(geo_url, params=geo_params)
  parsed_data = response.json()

  return parsed_data

def get_forecast(lat, lon):
  weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': key
  }

  response = requests.get(weather_url, params=weather_params)
  parsed_data = response.json()

  return parsed_data

def main():
  coords = get_geo_location('manchester')[0]
  forecast = get_forecast(coords['lat'], coords['lon'])

  print(len(forecast['list']))
  # print_json(data=forecast)

  return

if __name__ == "__main__":
  main()