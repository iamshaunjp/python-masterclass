# reading files

def read_file():
  # open file
  file = open('characters.txt', 'r')

  # read the file
  content = file.read()
  print(content)

  lines = file.readlines()
  for line in lines:
    print(line)

  # close the file
  file.close()

  return

def main():
  read_file()
  return

if __name__ == "__main__":
  main()
