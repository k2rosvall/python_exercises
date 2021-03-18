# USING WHILE LOOP WITH LISTS AND DICTIONARIES

#moving items from one list to another

# Start with users that need to be verfied,
# and and empty list to hold confirmed users.
unconfirmed_users = ['namjoon', 'seokjin', 'yoongi', 'hoseok', 'jimin', 'taehyung', 'jungkook']
confirmed_users = []

# Verfy each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
