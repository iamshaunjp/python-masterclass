#lists
names = ["mario", "peach", "luigi"]

print(names[0])
print(names[1])
print('length of the list is:', len(names))

# changing list values
names[1] = "toad"
print(names)

#list methods
names.append("bowser")
print(names)

names.remove("luigi")
print(names)

names.sort()
print(names)

