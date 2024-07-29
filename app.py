from pathlib import Path

# pathlib module

file = open('characters.txt', 'r')

def create_path():
  script_dir = Path(__file__).parent

  path = script_dir / 'characters'

  path.mkdir(parents=True, exist_ok=True)

  return

def main():
  create_path()

if __name__ == "__main__":
  main()
