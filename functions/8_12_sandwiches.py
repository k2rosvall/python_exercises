def make_sandwich(*ingredients):
    print("\nMaking a sandwich with:")
    for ingredient in ingredients:
        print("- " + ingredient)

make_sandwich('ham')
make_sandwich('ham', 'cheese', 'tomato')
make_sandwich('lettuce', 'turkey')