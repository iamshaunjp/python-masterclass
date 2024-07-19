# sets - unordered & unique elements
ingredients = {"tofu", "avocado", "cherries", "pasta", "tofu"}
print(ingredients)

# make a set using the set function around a list
scores = set([100, 25, 38, 100, 27])
print(scores)

# add and remove methods
ingredients.add("tomato")
ingredients.remove("cherries")
ingredients.discard("apple")

print(ingredients)

# joining sets (union)
set_one = {1, 2, 3}
set_two = {3, 4, 5}

union_set = set_one.union(set_two)
print(union_set)

# intersection (set of common elements)
int_set = set_one.intersection(set_two)
print(int_set)

# frozen (immutable) sets
ages = frozenset([19, 21, 35, 25])
print(ages)