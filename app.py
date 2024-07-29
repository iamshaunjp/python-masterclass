# writing data to files

characters = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_characters_to_file(filename):
  file = open(filename, 'w')

  for c in characters:
    file.write(c + "\n")

  file.close()


def main():
  write_characters_to_file('characters.txt')

if __name__ == "__main__":
  main()
