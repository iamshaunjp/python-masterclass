from pathlib import Path

# pathlib module

file = open('characters.txt', 'r')

def create_path():
  # directory path
  script_dir = Path(__file__).parent

  # file path
  path = script_dir / 'characters'

  # making the directory
  path.mkdir(parents=True, exist_ok=True)

  # making the file path
  path = path / 'zelda.txt'

  # file = path.open('w')
  # file.write("Ganon")

  # file = path.open('a')
  # file.write('\nLink')

  file = path.open('r')
  content = file.read()
  print(content)

  file.close()

  # convenience method for writing
  path.write_text('Epona')

  # convenience method for reading
  content = path.read_text()
  print(content)

  return

def main():
  create_path()

if __name__ == "__main__":
  main()
