count = 0

# break
# --> break out of loop

# while count < 10:
#   if count == 5:
#     break
#   print(count)
#   count += 1

# continue
# --> skip an iteration

while count < 10:
  count += 1
  if count % 2 != 0:
    continue
  print(count)