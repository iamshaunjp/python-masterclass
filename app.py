from rich import print_json
import requests

# fetching data
def get_posts(user_id=1):
  url = 'https://jsonplaceholder.typicode.com/posts'
  params = {
    "userId": user_id
  }

  response = requests.get(url, params=params)
  parsed_json = response.json()

  return parsed_json
  
def main():
  posts = get_posts(user_id=3)
  print_json(data=posts)

if __name__ == "__main__":
  main()