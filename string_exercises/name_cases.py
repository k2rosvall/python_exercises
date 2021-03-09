# 2-3 Personal Message: Store a person's name in a variable and print a message to that person.
name = "Hoseok"
print("Hello " + name + ", would you like to learn some Python today?")

# 2-4 Name Cases: Store a person's name in a variable and then print that person's name in lower, upper and title case
name = "kim namjoon"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5 Famous Quote Find a quote, print the quote and the name of its author.
quote = "\"Allow yourself to take it easy, take it one step at a time. You might discover the important things you were missing and they'll reach out to you\""
author = "Kim Seokjin"
print(author + " once said, " + quote)

# 2-6 Same but store in message
message = author + " once said, " + quote
print(message)

# 2-7 Stripping Names: store a person's name, and include some whitespace character at the beginning and end
name = " Park Jimin "
print(name)
print(name.lstrip())
print(name.strip())
print(name.rstrip())

