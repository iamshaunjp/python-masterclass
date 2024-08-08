import requests
from rich import print_json

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

  # complete challenge 2 here

  print(f'CSV weather report for {city} was created.')

def main():
  
  # CHALLENGE 1 - get the coordinates & forecast of a user city
  # --> ask the user what city they want the forecast report for in the terminal
  # --> fetch the geo coords of the city using the get_geo_location function
  # --> what happens when we try to get the coords of an invalid location?
  # --> handle this scenario before trying to fetch the forecast_data of the city

  # complete challenge 1 here

  # CHALLENGE 2 - use the forecast_data to create a CSV weather report
  # --> invoke the create_csv_report function and pass the city & forecast_data as arguments
  # --> create a file_path using the pathlib module, using the city name
  # --> loop through the entries in the forecast_data list (use forecast_data['list'])
  # --> write columns for the dt and the weather description
  # --> use entry['dt'] & entry['weather'][0]['description'] to get those values
  # --> bonus points for using pendulum (need to install) to format the dt values

  return

if __name__ == "__main__":
  main()