# closures
# a closure is a function that remembers values from its enclosing scope

def move_factory(character_name):
  uppercase_name = character_name.upper()

  def print_move(move_name):
    print(f"{uppercase_name} performs {move_name}!")
    
  return print_move


def main():
  ryu_move = move_factory('Ryu')

  ryu_move("Sweeping Slash")

if __name__ == "__main__":
  main()
