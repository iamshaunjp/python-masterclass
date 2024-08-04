import csv
from pathlib import Path

class BarTab:
  def __init__(self, table_number):
    self.table_number = table_number
    self.drinks = []
    self.total = 0
    self.tip = 0
    self.grand_total = 0
  
  def serve_user(self):
    while True:
      name = input("Drink name (or type 'f' to finish): ")
      if name.lower() == 'f':
        break
      
      try:
        cost  = float(input(f"{name} price: "))
      except ValueError:
        print("The price must be a number")
        continue
      
      self.drinks.append((name, cost))

  def calculate_totals(self):
    for _, cost in self.drinks:
      self.total += cost

    self.tip = self.total * 0.20
    self.grand_total = self.total + self.tip

  def create_csv(self):
    if not self.drinks:
      print("No drinks added. Exiting program.")
      return
    
    path = Path(__file__).parent / f"table_{self.table_number}.csv"

    with path.open('w', newline='') as file:
      writer = csv.writer(file)

      writer.writerow(["Drink name", "Cost"])
      writer.writerows(self.drinks)
      writer.writerow(['Total', self.total])
      writer.writerow(['Tip', self.tip])
      writer.writerow(['Grand Total', self.grand_total])

      print(f"The bar tab has been saved to {path}")


def main():
  tab = BarTab('7')
  print(f"New tab created for table {tab.table_number}")

  tab.serve_user()
  tab.calculate_totals()
  tab.create_csv()

  return

if __name__ == "__main__":
  main()