import requests
from rich import print_json

def get_something():
    url = "https://jsonplaceholder.typicode.com/xyz"

    try:
      response = requests.get(url)

      response.raise_for_status()

      parsed_data = response.json()
      return parsed_data
    
    except requests.exceptions.HTTPError as error:
      print(f"there was an HTTP error: {error}")
    except requests.exceptions.RequestException as error:
      print(f"there was an error: {error}")

def main():  
  data = get_something()
  print_json(data=data)

if __name__ == "__main__":
  main()