# Python has a special syntax for accessing the last element in a list.
# By asking for the item at index -1, Pyhon always returns the last item in the list:

bicycles = ['treck', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # Prints specialized

# This convention extends to other negative index values as well.
# The index -2 returns the second item from the end of the list
# the index -3 returns the third item from the end and so forth

# 3-1 Names: Store the names of a few of your friends in a list called names.
# Print each person's name by accessing each element in the list, one at a time.

names = ["Kim Namjoon", "Kim Seokjin", "Min Yoongi", "Jung Hoseok", "Park Jimin", "Kim Taehyung", "Jeon Jungkook"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

# 3-2 Greetings: Use the same list, print a message to them.
# The text of the message should be the same, but each message should be personalized with the person's name

print("Hello I'm " + names[0] + " from BTS")
print("Hello I'm " + names[1] + " from BTS")
print("Hello I'm " + names[2] + " from BTS")
print("Hello I'm " + names[3] + " from BTS")
print("Hello I'm " + names[4] + " from BTS")
print("Hello I'm " + names[5] + " from BTS")
print("Hello I'm " + names[6] + " from BTS")

# 3-3 Youw own list: prtin a serios of statemetns about these items.

print("BTS bias is " + names[3] + " a.k.a J-hope")
print(names[4] + " sings the song Serendipity")
print(names[0] + " is the leather of BTS")
print(names[1] + "'s nickname is WWH, WorldWide Handsome, you know?")
print("The maknae is " + names[-1])
print("V is the stage name of " + names[-2])
print("Suga is the stage name of " + names[2])

# adding elements to the list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorbikes = []
motorbikes.append("honda")
motorbikes.append("yamaha")
motorbikes.append("suzuki")

print(motorbikes)

# inserting elements at any position.
# You do this using insert(index, value)

motorbikes.insert(0, "ducati")
print(motorbikes)

# removing elements from a list

# use del when you know the position of the item

del motorbikes[0]
print(motorbikes)

# using pop() removes the last item in a list, but lets you work with that item after removing it

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# You can also use pop() to remove an item in a list at any position by including the index.

first_owned = motorcycles.pop(0)
print("The first motorocycle I owned was a " + first_owned.title())

# When you want to remove a value from a list and not use the item, use del, when you want to use it, use pop

# Removing an Item by Value

colors = ["blue", "black", "red", "green"]
print(colors)

colors.remove("red")
print(colors)

# NOTE. remove() only deletes the first occurrence of the value

# 3-4 Guest List: Make a list, then print a message to each person

guest_list = ["Ahn Hyejin", "Danielle Haim", "Dominique Provost-Chalkey"]

print("Hello " + guest_list[0] + ". I would like to invite you to my party")
print("Hello " + guest_list[1] + ". I would like to invite you to my party")
print("Hello " + guest_list[2] + ". I would like to invite you to my party")

# 3-5 Changing GUest List.

print(guest_list[1] + " can't make it to the party")

del guest_list[1]
guest_list.insert(1, "Jeon Jungkook")

print("Hello " + guest_list[0] + ". I would like to invite you to my party")
print("Hello " + guest_list[1] + ". I would like to invite you to my party")
print("Hello " + guest_list[2] + ". I would like to invite you to my party\n")

# 3-6 More guests

print("We found a bigger table!!!\n")

guest_list.insert(0, "Jung Hoseok")
guest_list.insert(2, "Park Jimin")
guest_list.append("Kim Seokjin")

print("Hello " + guest_list[0] + ". I would like to invite you to my party")
print("Hello " + guest_list[1] + ". I would like to invite you to my party")
print("Hello " + guest_list[2] + ". I would like to invite you to my party")
print("Hello " + guest_list[3] + ". I would like to invite you to my party")
print("Hello " + guest_list[4] + ". I would like to invite you to my party")
print("Hello " + guest_list[5] + ". I would like to invite you to my party\n")

# 3-7 Shrinking the Guest List.

print("Sorry, I'm only able to invite two people!\n")

print("I'm sorry " + guest_list.pop() + ", I can't invite you to dinner")
print("I'm sorry " + guest_list.pop() + ", I can't invite you to dinner")
print("I'm sorry " + guest_list.pop() + ", I can't invite you to dinner")
print("I'm sorry " + guest_list.pop() + ", I can't invite you to dinner\n")

print(guest_list[0] + ". You're still invited to dinner!")
print(guest_list[1] + ". You're still invited to dinner!")

del guest_list[0]
del guest_list[0]

print(guest_list)

# Sorting a list permanently with sort() alphabetically

cars = ["bmw", "audi", "hyundai", "toyota"]
cars.sort()
print(cars)

# Reverse order

cars = ["bmw", "audi", "hyundai", "toyota"]
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with sorted(), can also accept reverse=True

cars = ["bmw", "audi", "hyundai", "toyota"]

print("\nHere is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\nHere is the original list again: ")
print(cars)

# Printing a list in reverse order, changes permanently

numbers = ["7", "100", "2", "10", "15"]
numbers.reverse()
print(numbers)

# Finding length of a list
print("The length of numbers is " + str(len(numbers)))

# 3-8 Seeing the world.
locations = ["Seoul", "Hawaii", "London", "Thailand", "Busan", "Tokyo", "Okinawa"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3-9 Dinner Guests

guest_list = ["Ahn Hyejin", "Danielle Haim", "Dominique Provost-Chalkey"]

print("I'm inviting " + str(len(guest_list)) + " people to dinner")

# 3-10 Every function

bts_songs = ["Save ME", "Run", "Dyonisus", "Boy With Luv", "Attack on Bangtan", "No More Dream", "Intro: Persona", "Moon"]

print(bts_songs)
# append
bts_songs.append("Filter")
bts_songs.append("Begin")
bts_songs.append("Dynamite")

print(bts_songs)

# insert
bts_songs.insert(3, "Stigma")
bts_songs.insert(6, "Trivia: Seesaw")

print(bts_songs)

# del

del bts_songs[2]
print(bts_songs)

# pop
popped_song = bts_songs.pop()
print(popped_song + " was removed from bts_songs")
print(bts_songs)

# remove
bts_songs.remove("No More Dream")
print(bts_songs)

# sorted
print(sorted(bts_songs))
print(sorted(bts_songs, reverse=True))

# sort
bts_songs.sort()
print(bts_songs)
bts_songs.sort(reverse=True)
print(bts_songs)

# reverse
bts_songs.reverse()
print(bts_songs)
bts_songs.reverse()
print(bts_songs)

# len

print("The length of the list is " + str(len(bts_songs)))
