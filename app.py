# single line comment

'''
multi-line comments
use double or single quotes x 3
'''

# declaring variables
name = "mario"
age = 30
height = 5.4

name = "luigi"
age = 32
height = "Five ft, 4 in."

# printing variables
print(name, age, height)

# type errors
print(name + " is " + str(age))
print(10 + int("20"))

# string methods
greeting = "  Hello, Ninjas!  "

print(len(greeting))
print(greeting.strip())
print(greeting.strip().lower())
print(greeting.strip().upper())
print(greeting.replace("Hello", "Yo").strip())
print(greeting)