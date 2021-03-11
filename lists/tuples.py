# A tuple is an immutable list

# Defining a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
# You can assign a new value to a variable that holds the tuple

print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

print("\n")

dimensions = (400, 100)
print("Modified dimensions: ")
for dimension in dimensions:
    print(dimension)

# When compared with lists, tuples are simple data structures.
# Use them when you want to store a set of values that should not be changed through out the life of a program

print("\n")

# 4-13 Buffet.
buffet_foods = ("eggs", "soup", "salad", "meat", "pasta")
for food in buffet_foods:
    print(food)
print("\n")
# buffet_foods[0] = "jelly"

buffet_foods = ("pizza", "soup", "salad", "meat", "fish")
for food in buffet_foods:
    print(food)

