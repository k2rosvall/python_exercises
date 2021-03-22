# Return values
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('yoongi' , 'min')
print(musician)

# Making argument optional
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name2('Hoseok', 'jung')
print(musician)

# using a function with a while loop

while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
