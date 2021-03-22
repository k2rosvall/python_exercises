# Positional arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword arguments
describe_pet(animal_type='cat', pet_name='silvestre')
describe_pet(pet_name='uri', animal_type='goldfish')

# Default values
def describe_pet_default(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_default(pet_name='willie')
