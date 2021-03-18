# Using int() to accept NUmerical Input

height = input("How tall are you? ")
height = int(height) # int() converts the string to numerical value

if height >= 160:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

