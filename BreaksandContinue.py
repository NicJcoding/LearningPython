# Breaks

"""
color = ["Black", "White", "Orange", "yellow"]

for i in color:
    print(i)
    if i == "White":
        print(True)
        break

string = ""
while True:
    user_input = input("Enter characters: ")
    if user_input == "quit":
        print(string)
        break

string = string + user_input
    """

# Continue Statement
""" 
for i in range(1,11):
    if i % 3 == 0:
        continue

    print(i)


counter = 1
while counter <= 10:
    
    if counter % 2 == 0:

        counter += 1
        continue
    print(counter)
    counter += 1
"""

# Pass Statement - still goes through whether true or false - placeholder for the future code.

for i in range(1,11):
    pass
