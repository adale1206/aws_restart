myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


age = input("How old are you? ")
print("{}, {} years old, you like the the color {} and you have a {}.".format(name,age,color,animal))
animalname = input("What is the name of your pet? ")
print("You have a {} and you named it {}." .format(animal,animalname))
