alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# adding nw key-value pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# empty dictionary
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

# modifying values
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'])

alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'])

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_3['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_3['x_position'] += x_increment

print("New x-position: " + str(alien_3['x_position']))

# removing key-value pairs
alien_4 = {'color': 'green', 'points': 5}
print(alien_4)

del alien_4['points']
print(alien_4)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title())

# 6-1 Person
person = {'first_name': 'hoseok', 'last_name': 'jung', 'age': 27, 'city': 'seoul'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2 Favorite Numbers
favorite_numbers = {
    'namjoon': 7,
    'seokjin': 3,
    'yoongi': 6,
    'hoseok': 15,
    'jimin': 13,
    'taehyung': 2,
    'jungkook': 1,
}

print("Namjoon's favorite number is " + str(favorite_numbers['namjoon']))
print("Seokjin's favorite number is " + str(favorite_numbers['seokjin']))
print("Yoongi's favorite number is " + str(favorite_numbers['yoongi']))
print("Hoseok's favorite number is " + str(favorite_numbers['hoseok']))
print("Jimin's favorite number is " + str(favorite_numbers['jimin']))
print("Taehyung's favorite number is " + str(favorite_numbers['taehyung']))
print("Jungkook's favorite number is " + str(favorite_numbers['jungkook']))

# 6-3 Glossary:
glossary = {
    'variable': "a variable is a place where you store information",
    'if': 'an if is a conditional',
    'loop': 'a loop is something that gets repeated over and over again',
    'dictionary': 'is a structure where you store stuff'
}

print("variable: " + glossary['variable'])
print('if: ' + glossary['if'])
print("loop: " + glossary['loop'])
print("dictionary: " + glossary['dictionary'])

# looping through

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key + ", Value: " + value)

# looping through keys

for name in favorite_languages.keys(): # same as for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see you favorite language is " + favorite_languages[name].title())

# Looping through keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the pool")

# Looping through all values in a dictionary
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

# Recovering unique items
favorite_languages = {
    'jen': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

# 6-4 Glossary 2:
for key, value in glossary.items():
    print(key.title() + ": " + value + ".")

# 6-5 Rivers:
rivers = {
    'han river': 'south korea',
    'nile': 'egypt',
    'thames': 'england',
}

for key, value in rivers.items():
    print("The " + key.title() + ", runs through " + value.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6 Polling
people = ['hoseok', 'jimin', 'jungkook', 'namjoon', 'jen', 'phil', 'sara', 'seokjin', 'taehyung', 'yoongi', 'edward']

for person in people:
    if person in favorite_languages.keys():
        print("Thank you for responding!")
    else:
        print("Please respond our poll")


# List of dictionaries
print("\n")
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Make 30 green aliens:
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# Modifying aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# A list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
      " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

