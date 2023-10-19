# While loops
"""
 i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Loop is done.")
"""

""" secret_number = 6
guess = 0
attempts = 0

# while attempts is less than 3 and guess is not equal to secret number then the code will keep going.
# If guess is equal to the secret number or the number of attempts hits 3, the code will finish the while loop
while attempts < 3 and guess != secret_number:
    guess = int(input("Guess a number between 1 - 10: "))
    if guess == secret_number:
        print("You guessed it correctly!")
    else:
        print(" You guessed incorrectly!")
        attempts = attempts + 1
"""

# For Loops - used to go through things like lists, typically
# For item in variable: - starts loops
colors = ["black", "green", "purple", "grey"]
name = "nicolas"

# prints out each element separately
for item in colors:
    print(item)

# prints out each character separate
for item in name:
    print(item)

# range - will run the loop 6 times but not include the 6th time. Since it starts at 0
for i in range(6):
    print(i)
# range starts at 1 but ends at 7.
for i in range(1,7):
    print(i)
# range starts at 3 and ends at 4.
for i in range(3,5):
    print(i)

# Range can skip numbers for counting but adding a 3rd parameter
# I am telling it to skip by 2 - the third number does this - it will start at 0 but end at 18.
for i in range (0,20,2):
    print(i)

print("---------------------")
# Practice problem for "For loop"  -  make a grocery list and add the cost.
item_cost = [4,6,3,2]
total = 0
for i in item_cost:
    total = total + i
    print(total)






