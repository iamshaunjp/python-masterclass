# arguments
def multiply(a, b):
  return a * b

result = multiply(7, 5)
print(result)

# named arguments
def print_score(name, score):
  print(f"{name} has a score of {score}")

print_score("yoshi", 75)
print_score(score=90, name="mario")

# default arguments
def divide(a, b = 2):
  return a / b

result = divide(20, 4)
print(result)

result = divide(50)
print(result)