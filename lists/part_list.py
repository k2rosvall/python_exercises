# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]

print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-2:])

# Looping through a slice
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

my_foods.append("Tamales")
friend_foods.append("Sushi")

print(my_foods)
print(friend_foods)
print("\n")

# 4-10 Slices.
bts_members = ["kim namjoon", "kim seokjin", "min yoongi", "jung hoseok", "park jimin", "kim taehyung", "jeon jungkook"]

print("The first three items in the list are: ")
print(bts_members[:3])
print("\nThe three items from the middle of the list are:")
print(bts_members[2:5])
print("\nThe last three items from the list are: ")
print(bts_members[-3:])

# 4-11 My Pizzas, Your Pizzas
my_pizzas = ["mushroom", "pepperoni", "supreme"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("sausage")
friend_pizzas.append("hawaiian")

print("\nMy favorite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

print("\n")

# 4-12 More Loops
for pizza in my_pizzas:
    print(pizza.title() + " is my favorite pizza!")

print("\n")

for pizza in friend_pizzas:
    print(pizza.title()  + " is my friend's favorite pizza!")


