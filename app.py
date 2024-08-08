import requests
from rich import print_json
from pathlib import Path
import csv
import pendulum

def get_geo_location(city):
  geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
  geo_params = {
    'q': city,
    'appid': '28d4883cb180676d90561d43c5caa22f'
  }

  response = requests.get(geo_url, params=geo_params)
  parsed_data = response.json()
  return parsed_data

def get_forecast(lat, lon):
  weather_url = "https://api.openweathermap.org/data/2.5/forecast"
  weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': '28d4883cb180676d90561d43c5caa22f'
  }

  response = requests.get(weather_url, params=weather_params)
  parsed_data = response.json()
  return parsed_data

def create_csv_report(city, forecast_data):
  file_name = city.lower().replace(' ', '')
  file_path = Path(__file__).parent / f"{file_name}.csv"

  with file_path.open('w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date / Time", "Weather Description"])

    for entry in forecast_data['list']:
      datetime = entry['dt']
      description = entry['weather'][0]['description']
      pdt = pendulum.from_timestamp(datetime)

      writer.writerow([pdt.to_day_datetime_string(), description])

  print(f'CSV weather report for {city} was created.')

def main():

  city  = input("Create weather report for which city?: ").strip()
  coords = get_geo_location(city)[0]
  
  if not coords:
    print("That is not a valid city, sucker!")
    return
  
  forecast_data = get_forecast(coords['lat'], coords['lon'])
  print_json(data=forecast_data)

  create_csv_report(city, forecast_data)

  return

if __name__ == "__main__":
  main()