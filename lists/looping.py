# LOOPS
# Looping through an entire list

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# 4-1 Pizzas.
pizzas = ["Pepperoni", "Mushroom", "Supreme", "Hawaiian", "Italian"]

for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("\nI really love pizza!!!!")

# 4-2 Animals.
animals = ["dog", "cat", "turtle", "hamster"]
for animal in animals:
    print("A " + animal + " would make a great pet")

print("\nAny of these animals would make a great pet")

# range() function
for value in range(1, 5):
    print(value)

# using list() function.
numbers = list(range(1, 6))
print(numbers) # prints a list

even_numbers = list(range(2, 11, 2)) # starts in two and adds two to the value until 11
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2 # exponent
    squares.append(square)

print(squares)

cubics = []
for value in range(1,11):
    cubics.append(value**3)
print(cubics)

# MIN, MAX, SUM
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45

# LIST COMPREHENSIONS
# A list comprehension combines the for loop and the creation of new elements into one line and
# automatically appends each new elements.

squares = [value**2 for value in range(1, 11)]
print(squares)

# 4-3 Counting to twenty
for value in range (1, 21):
    print(value)

# 4-4 One million
numbers = list(range(1, 1000001))
#for number in numbers:
    #print(number)

# 4-5 Summing a million.
print("Min: " + str(min(numbers)))
print("Max: " + str(max(numbers)))
print("Sum: " + str(sum(numbers)))

# 4-6 Odd Numbers.
odd_numbers = list(range (1, 21, 2))
for value in odd_numbers:
    print(value)

# 4-7 Threes.
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# 4-8 Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

# 4-9 Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
