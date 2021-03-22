# 8-9 magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


# 8-10
def make_great(magicians):
    great_magicians = []
    while magicians:
        great_magician = magicians.pop().title() + " the Great"
        great_magicians.append(great_magician)

    for magician in great_magicians:
        magicians.append(magician)


magicians = ['hoseok', 'jimin', 'taehyung']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
