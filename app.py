from rich import print_json
import requests

# fetching data
def get_posts():
  url = 'https://jsonplaceholder.typicode.com/posts'

  response = requests.get(url)
  parsed_json = response.json()

  return parsed_json
  
def main():
  posts = get_posts()
  print_json(data=posts)

if __name__ == "__main__":
  main()