name = "ada lovelace"
print(name.title())  # capitalizes the words
print(name.upper())  # to Uppercase
print(name.lower())  # to Lowercase
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello " + full_name.title() + "!")
message = "Hello " + full_name.title() + "!"
print(message)
# add tab to text
print("\tPython")
# New line
print("Languages:\nPython\nC\nJavascript")
# Eliminates whitespace at the right end of the string, rstrip()
favorite_language = "Python "
print(favorite_language) # prints 'Python '
print(favorite_language.rstrip()) # prints 'Python'
# To remove permanently you store the stripped value back into the variable
favorite_language = favorite_language.rstrip()
# You can also use lstrip() for space on the left side or strip() from both sides
