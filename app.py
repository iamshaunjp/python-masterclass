from pathlib import Path

def serve_user():
  drinks = []

  while True:
    name = input("Drink name (or type 'f' to finish): ")
    if name.lower() == 'f':
      break
    
    try:
      cost  = float(input(f"{name} price: "))
    except ValueError:
      print("The price must be a number")
      continue
    
    drinks.append((name, cost))

  return drinks

def main():
  # get table number from user
  try:
    table_no = int(input("Table number: "))
    print(f"Starting a tab for table {table_no}")
  except:
    print("Not a valid table number. Exiting program.")
    return
  
  # create file path using table number
  path = Path(__file__).parent / f"table_{table_no}.csv"

  # get items from user (drink name and price)
  drinks = serve_user()
  
  # calculate the totals (total, tip, grand_total)


  # create the csv

  return

if __name__ == "__main__":
  main()