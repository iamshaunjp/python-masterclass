# dictionaries
person = {
  "name": "yoshi",
  "age": 30,
  "job": "egg collector"
}

print(person["name"])
print(person["age"])

# methods
print(person.get("name"))

print(person.keys())
print(person.values())
print("age" in person.keys())

copied_person = person.copy()
print("copied person:", copied_person)

person.update({"name": "mario", "age": 35})
print("updated person:", person)

person.clear()
print('cleared person:', person)
