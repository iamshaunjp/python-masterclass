# higher order functions -> more reusable & modular

def ninja_action(action, x):
  return action("ninja", x)

def attack(character, x):
  return f"The {character} attacks with a strength of {x}"

def defend(character, x):
  return f"The {character} defends with a block power of {x}"

action_one = ninja_action(attack, 5)
action_two = ninja_action(defend, 7)
print(action_one)
print(action_two)

# built-in higher order functions
# 1 - map function

moves = ['punch', 'kick', 'block', 'dodge']

def make_move_powerful(move):
  return f"{move.upper()}!!!"

powerful_moves = map(make_move_powerful, moves)
print(list(powerful_moves))

# 2 - filter function

scores = [20, 95, 45, 85, 90, 15, 55, 100, 10]

def is_high_score(score):
  return score >= 90

high_scores = filter(is_high_score, scores)
print(list(high_scores))