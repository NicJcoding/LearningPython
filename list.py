# Understanding basic list

family = ["Nic", "Bailey", "Athena", "FutureKid"]
age = [24, 23, 4]
booleans = [True, False, True, True]
mixed_lists = ["Nic", 24, True]


# Getting the index from the list - remember the index would be a element for a list
print(family[0])
print(family[-1])


# How to edit an element
family[0] = "New Nic"
print(family)

# Changing it back
family[0] = "Nic"
print(family)

# Getting the lengths of a list - 3 elements starting with 1
print(len(family))

# Grabbing the elements from a certain index
# grabs index 1 and 2 but not 3
print(family[1:3])

# Grabbing index again
print(family[:4])

# List Methods
# .append - adds to the end of the list
family.append("Juarez")
print(family)

# .clear - removes all the elements on the list and keeps an empty bracket
# family.clear()
# print(family)

# .count - lets you count the number of elements that have the exact same thing.
print(family.count("n")) # does not work
print(family.count("Nic"))

# .index will grab the index of an element
print(family.index("Athena"))

# . insert - will insert an element ( 2,random) adds the element at index 2
family.insert(2, "Random")
print(family)

# .pop - remove an element at a specified position
family.pop(2)
family.pop(3)
print(family)

# .remove - will remove the first element that matches
family.remove("Juarez")
print(family)

# .reverse - reverse a list - 1,2,3 ---> 3,2,1
family.reverse()
print(family)

# .sort - will sort a list from least to greatest. List of strings will sort alphabetical
# numbers will sort from least to greatest
family.sort()
print(family)

# .copy - gives you a copy of the list
familyCopy = family.copy()
print(familyCopy)


