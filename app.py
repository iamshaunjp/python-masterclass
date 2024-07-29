# appending to a file

more_characters = ["Diddy Kong", "Donkey Kong", "Wario"]

def write_characters_to_file(filename):
  # open file
  file = open(filename, 'a')

  # append to file
  for c in more_characters:
    file.write(c + "\n")

  # close file
  file.close()

  return

def main():
  write_characters_to_file('characters.txt')

if __name__ == "__main__":
  main()