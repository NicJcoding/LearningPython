# If, else and elif
""" good_weather = False
bad_weather = True

if good_weather:
    print("Go to the beach.")
elif bad_weather:
    print(" Stay at home and do homework.")
else:
    print("Go on a walk.")
"""

# Logical Operators - and, or
# and - both need to be tru e
# or - one or the other need to be true
# not - will flip the boolean ( true to false or false to true)
"""
 is_hungry = True
is_thirsty = True

if is_hungry and is_thirsty:
    print("Eat and drink something")
 """

# Comparison operators

""" num = -6
if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is 0.")
elif num < 0:
    print("This number is negative.")
else:
    print("This is not a number.")


age = 18

if age >= 18:
    print(" You are an adult.")
else:
    print(" You are a minor")
"""

# Practice Problem
total_classes = input ("Number of classes held?")
total_attended = input("Number of classes attended?")

student_attendance_rate =  int(total_attended) / int(total_classes)
student_percentage: float = student_attendance_rate * 100

if student_percentage >= 75:
    print("The student has a class attendance percentage of " + str(student_percentage) + "%")
    print(". They have passed the course!")
else:
    print("The student has a class attendance percentage of " + str(student_percentage) + "%")
    print("They have failed the course!")