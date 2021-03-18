prompt = "\nEnter the toppings you want to add:"
prompt += "\n (when done type 'quit'. "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print("Adding " + topping.title())

