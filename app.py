# global & local variables

x = 10

def print_x():
  global x

  x = 5
  print(f"x inside the print_x func is {x}")

def print_y():
  y = 20
  print(f"y inside the print_y func is {y}")

print_y()
print_x()
print(f"global value of x is {x}")


# scope within nested functions

def outer():
  age = 25

  def inner():
    nonlocal age

    age = 30
    print(f"age inside inner() is {age}")

  inner()
  print(f"age inside outer() is: {age}")
  
outer()