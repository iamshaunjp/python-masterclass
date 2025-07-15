# declaring variables
name= "maria" # string variables
age = 30 #integer variable
height = 5.4 #float variable which is a decimal number

#printing variables
print(name, age, height)

#variable can change at anytime by assigning new values
name="Lucas"
age= 35
height = 1.7
print(name, age, height)

#type error
print (name + " is " + str(age)) #type casting to string

print(10 + int("20")) #type casting to integer


#string methods
greeting = "    Hello , Ninja"

print(len(greeting)) #len is a built in function for finding length of characters
print(greeting.strip()) # string method being used to remove space
print(greeting.strip().lower())
print(greeting.strip().upper())
print(greeting.replace("Hello", "Yo").strip())
