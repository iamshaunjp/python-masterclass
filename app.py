# return values

def square(x):
  return x * x

result = square(5)
print(result)

# returning multiple values

def get_coords():
  x = 25.5
  y = 48.2
  return x, y

x, y = get_coords()
print(x, y)

# using return to break out of a function

age = 19

def do_something():
  if age < 20:
    return None
  print(age)

result = do_something()
print(result)