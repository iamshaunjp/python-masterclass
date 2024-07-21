# example without error handling

# example 1

try:
  number = int(input("Enter a number: "))
  print('You entered:', number)
except ValueError as e:
  print('That is not a number')
  print('error:', e)
finally:
  print('completed')

# example 2

a = 10
b = 0

try:
  print(a / b)
except ZeroDivisionError as e:
  print('cannot divide a number by 10')
  print('error:', e)

print('end of the file')