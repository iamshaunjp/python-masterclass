# CHALLENGE: Shopping list formatter

shopping_list = []

# SECTION ONE - creating the shopping list
while True:
    
  item = input("Enter an item (or 'q' to quit): ")
  if item == 'q':
    break
  
  # Challenge: ask user for price (int)
  # handle any ValueError by printing a message, skipping a loop and asking for a new item

  try:
    price = int(input("Enter the price (£) of the item: "))
  except ValueError as e:
    print("That is not a valid number.")
    continue

  shopping_list.append((item, price))

# SECTION TWO - formatting the shopping list
total = 0

for item, price in shopping_list:
  print(f"{item} - £{price}")
  total += price

print(f"total price: £{total}")

# Challenge: use a for loop to print each item and price on its own line
# after all items have been output, also print out the total price
