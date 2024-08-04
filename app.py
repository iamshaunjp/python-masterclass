import pendulum

def main():
  pdt = pendulum.now()
  print(pdt)

  # formatting with pendulum
  print(pdt.format('DD/MM/YYYY'))
  print(pdt.format('H:m A'))
  print(pdt.to_day_datetime_string())

  # other pendulum methods
  pdt2 = pdt.add(days=1, months=2, years=3)
  print(pdt2.to_day_datetime_string())

  pdt3 = pdt.subtract(years=4, weeks=1)
  print(pdt3.to_day_datetime_string())

  pdt4 = pdt.set(year=1986, month=4)
  print(pdt4.to_day_datetime_string())

if __name__ == "__main__":
  main()