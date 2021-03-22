# 8-11 unchanged magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []
    while magicians:
        great_magician = magicians.pop().title() + " the Great"
        great_magicians.append(great_magician)

    for magician in great_magicians:
        magicians.append(magician)

    return magicians


magicians = ['hoseok', 'jimin', 'taehyung']
new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
