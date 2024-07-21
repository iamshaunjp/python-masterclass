# match case statements --> 3.10

belt_color = input("What is your ninja belt color: ")

match belt_color:
  case "white":
    print("Ninja Fledgling")
  case "red":
    print("Intermediate Ninja")
  case "blue":
    print("Advanced Ninja")
  case "purple":
    print("Pro Ninja")
  case "black":
    print("Master Ninja")
  case _:
    print("Belt color is unknown")