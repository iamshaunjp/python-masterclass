import csv
from pathlib import Path

class BarTab:
  def __init__(self, table_number):
    self.table_number = table_number
    self.drinks = []
    self.total = 0
    self.tip = 0
    self.grand_total = 0

def main():
  tab = BarTab('7')
  print(f"New tab created for table {tab.table_number}")

  return

if __name__ == "__main__":
  main()