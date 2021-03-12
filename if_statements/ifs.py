cars = ["audi", "bmw", "subaru", "hyundai", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
# checking inequality
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("\nHold the anchovies!\n")

# numerical comparisons
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again\n")

# checking multiple conditions

#and
age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
    print("true")
else:
    print("false")

#or

if age_0 >= 21 or age_1 >= 21:
    print("true")

# Checking whether a value is in a list

requested_topping = ["mushrooms", "onions", "pineapple"]

if "mushrooms" in requested_topping:
    print("TRUE")
# Checking whether a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

# 5-1 COnditional tests
car = "subaru"
print("\nIs car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5-2 More conditional tests
name = "Jimin"

if name == "Jimin":
    print("Hello Jimin!")

name = "Hoseok"
if name != "Jimin":
    print("You're not Jimin!")

username = "HobiLover02"
if username.lower() == "hobilover02":
    print("Welcome HobiLover02")

music_wins = 12

if music_wins >= 32:
    print("Hello Dynamite!!!")
else:
    print("You're not Dynamite!!!!\n")

# if-else
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18!\n")


# if-elif-else chain
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

# better code

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $"+ str(price) + ".")

# 5-3 ALien Colors #1
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points!!!!\n")

# 5-4 Alien Colors #2
alien_color = "yellow"
if alien_color == "green":
    print("you just earned 5 points!")
else:
    print("you just earned 10 points!!!")

# 5-5 alien colors #3
alien_color = "red"

if alien_color == "green":
    print("you just earned 5 points!")
elif alien_color == "yellow":
    print("you just earned 10 points!")
elif alien_color == "red":
    print("you just earned 15 points!")


# 5-7 Favorite fruit:
fruits = ["banana", "apple", "grapes", "watermelon"]

if "banana" in fruits:
    print("you really like bananas!")

if "orange" not in fruits:
    print("You don't like oranges :(")

# ifs with lists

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print("Adding "+ requested_topping)

print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("sorry, we are out of green peppers right now")
    else:
        print("Adding "+ requested_topping)

print("\nFinished making your pizza!\n")

# checkin that a list is not empty

requested_topping = []

if requested_topping:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping)

    print("\nFinished making your pizza!")
else:
    print("are you sure you want a plain pizza?\n")

# checking multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5-8 Hello admin
usernames = ['HobiLover02', 'jiminlicious', 'rkivemono', 'rjAlpaca', 'goldenMaknae', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again")
else:
    print("We need to fine some users!!!!")

# 5-10 Checking usernames
current_users = ['hobilover02', 'minsuga', 'jiminlicious', 'goldenmaknae', 'rkivekoya', 'rjalpaca', 'tatabear']
new_users = ['jihopeline', 'capitanmentalstability', 'blumkii', 'roxeniteii', 'tatabear']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("please enter a new username")
    else:
        print("username available")



