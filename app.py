from pathlib import Path

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
  print(path)

  # get items from user (drink name and price)

  
  # calculate the totals (total, tip, grand_total)


  # create the csv

  return

if __name__ == "__main__":
  main()