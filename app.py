# for loops with lists --> iterate a collection or range

names = ["yoshi", "mario", "luigi", "peach"] # iterable

for name in names:
  print(name)

for name in names:
  if name == 'luigi':
    break
  print(name)

for name in names:
  if name == 'mario':
    continue
  print(name)

# for loop with strings

for letter in "ninja":
  print(letter.upper())