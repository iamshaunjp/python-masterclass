score = 4

# if statements

# if score > 5:
#   print('the score is greater than 5')

# if/else statements

# if score > 10:
#   print('the score is greater than 10')
# else:
#   print('the score is not greater than 10')

# if/elif/else statements

if score > 10:
  print('the score is greater than 10')
elif score > 5:
  print('the score is greater than 5, but not greater than 10')
else:
  print('the score is 5 or less')

# AND, OR, NOT, IS NOT

age = 20

if age > 12 and age < 20:
  print('teenager')

if age < 13 or age > 19:
  print('not a teenager')

authenticated = True

if not authenticated:
  print('you are not authenticated')

if authenticated is True:
  print('you are authenticated')