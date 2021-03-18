sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'vegan', 'pastrami', 'pork', 'egg']
finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("\nMade sandwiches: ")
for sandwich in finished_sandwiches:
    print(sandwich)
