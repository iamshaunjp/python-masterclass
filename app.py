# lists
names = ["mario", "peach", "luigi"]

print(names[0])
print(names[1])
print('length of the list is:', len(names))

# changing list values
names[1] = "toad"
print(names)

# list methods
names.append("bowser")
print(names)

names.remove("luigi")
print(names)

names.sort()
print(names)

# tuples
top_scores = (100, 95, 92, 92, 88, 85)

print(top_scores[0])
print(top_scores[2])
print("the length of the tuple is:", len(top_scores))

# tuples are immutable
# top_scores[0] = 99

# tuple methods
print(top_scores.count(92))
print(top_scores.index(85))