# Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # tells python to ignore the rest of the code

    print(current_number) # prints only odd numbers

