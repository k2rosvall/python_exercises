prompt = "\nWhat's your age? "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("\nThe ticket is free!")
    elif age <= 12:
        print("\nThe ticket costs $10")
    elif age > 12:
        print("\nThe ticket costs $15")