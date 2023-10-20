# Learning Functions
# Block of code that we store into a function - stores a task to be used over and over again.
# To start a function you need to start it with Def

def say_hello():
    print("Hello User!")


say_hello()

""" def intro():
    greet = input("Hello, my name is Nicolas. What is your name? ")
    print("Nice to meet you, " + greet + "!")


intro()
"""

# Adding Parameters - placeholder for a value in the ()

""" def friends(name, name2):
    print("Hello! " + name + " and " + name2)


friends("Nicolas", "Bailey")


# Return statement
# Once you use return. nothing will execute after it. Return will end the function.
def add_two_num(num, num2):
    return num + num2


total = add_two_num(4, 6)
print(total)
"""


def calculation(a, b, sign):
    if sign == "+":
        print(a + b)
    elif sign == "-":
        print(a - b)


calculation(4, 4, "+")


def showEmployee(name, salary):
    print("Employee " + name + ", salary  is: " + str(salary))


showEmployee("Sam", 90000)


def outer(a, b):
    def inner(a, b):
        return a + b
    total = inner(a,b)
    return total + 8

result = outer(5,10)
print(result)

"""
string = ("racecar")
print(string)
reverse_string = string[::-1]
print(reverse_string)

"""


def check_reverse(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)


check_reverse("racecar")
check_reverse("hello")
check_reverse("Nicolas")
check_reverse("kayak")
