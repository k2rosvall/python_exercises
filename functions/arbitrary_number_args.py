# Passing an Arbitrary Number of Arguments

# *toppings creates a tuple
def make_pizza(*toppings):
    # print(toppings)
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mixing positional and arbitrary arguments
def make_pizza2(size, *toppings):
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza2(16, 'pepperoni', 'ham')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')