"""Basic print from python"""

print("Juarez")
print(3)
print(5 + 5)

# Learning Variables in Python

numOfApples = 20
myName = "Nicolas"
print(numOfApples)
print(myName)

# Renaming Variables
myName = "Bailey"
print(myName)

myName = 24
print(myName)

# Data Types - strings
sentence = "This is a string"
print(type(sentence))

# Data types - Integers
numOfApples = 3
print(type(numOfApples))

# Data types - Floats
grade = 96.5
print(type(grade))

# Data types - Booleans ( T or F)
isRaining = False
isHot = True
print(isRaining)
print(type(isRaining))
print(type(isHot))
print(isHot)

# Converting Data Types

# Float to Integer
floatNumber = 5.678

# Takes the float and strips away the decimals ( does not round)
print(int(floatNumber))

# Integer to Float
IntNumber = 4
print(float(IntNumber))

# String
thisISaString = "Hello"
print(str(thisISaString))

# Converting String into Integer ( Only works with number strings)
numberString = "4"
print(int(numberString))

# Section 2 of class

# Concatenation (Combination of strings)
# String conacatenation can only be done with strings
first_name = "Nicolas"
last_name = " Juarez"
age = 24

full_name = first_name + last_name
print(full_name)

print("My name is " + full_name +". I am " + str(age) + " years old!")



# Index start at 0

message = "Hello World"
#        0123456789 ( This would be the index of the characters
# How to access index character, you use [];
print(message[4])
print(message[0])

# How to start from the end
# use-1 backwards
print(message[-1])
print(message[-2])
print(message[-3])
print(message[-4])
print(message[-5])
print(message[-5])

# Finding the length of variable
# Function is len()
print(len(message))

# .find() allows you to grab the index of a character
# Will find the first letter
print(message.find("l"))
# If will find first letter for the word
print(message.find("World"))

# If you get -1, it was not able to find the index
print(message.find("x"))

# .replace()
# Will take part of the string and replace with what I want
print(message.replace("Hello","Goodbye"))

# .lower()
# Will lowercase everything
print(message.lower())

# .upper()
# Will make everything uppercase
print(message.upper())

# capitalize()
# Capitalizes the first letter of the string and will lowercase the rest of the string
print(message.capitalize())

# Math Functions
# round() - will round the number
# absolute - abs() will make neg into positive
# pow (base, exponent) pow(2,4) 2 to the power of 4

# Inputs
# It will print this prompt to the user, and they will respond.
# We need to store the users answer to a variable which is name
# We can then print a statement to respond
# Whenever we use input --- all the responses will  be a string.
name = input("What is your name? ")
age = input("What is your age?")
print("Hi " + name + "!" + " You are " + age + " years old!")







