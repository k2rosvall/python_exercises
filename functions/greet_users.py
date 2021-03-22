# passing a list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hobi', 'jimin', 'namjoon']
greet_users(usernames)