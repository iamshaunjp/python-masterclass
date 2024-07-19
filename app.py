# formatted strings (f-strings)
name = "mario"
score = 50

# examples - newer
print(f"{name} has a score of {score}")

# older approach
print("{} has a score of {}".format(name, score))
print("{1} has a score of {0}".format(name, score))
print("{n} has a score of {s}".format(n=name, s=score))

# expressions in f-strings
print(f"{name.capitalize()} has a bonus score of {score * 2}")