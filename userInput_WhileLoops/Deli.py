sandwich_orders = ['pastrami', 'turkey', 'vegan', 'pork']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("\nMade sandwiches: ")
for sandwich in finished_sandwiches:
    print(sandwich)
