# lambda functions

def main():
  # example 1

  add_stuff = lambda x, y: 10 + x + y
  result = add_stuff(5,7)
  print(result)

  # example 2 - with built in HO function

  scores = [20, 95, 45, 85, 90, 15, 55, 100, 10]

  high_scores = filter(lambda score: score >= 90, scores)
  print(high_scores)
  print(list(high_scores))


if __name__ == "__main__":
  main()
