responses = {}

while True:
    name = input("\nWhat's your name? ")
    response = input("Where would you like to go on vacation? ")

    responses[name] = response

    keep_asking = input("Would you like someone else to take the pool? (yes/no) ")
    if keep_asking == 'no':
        break

print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + ".")