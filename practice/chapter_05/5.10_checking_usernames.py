current_users = ['tom', 'jerry', 'admin', 'tony', 'mary']
new_users = ['sandford', 'talor', 'Admin', 'eric', 'mary']

# current_users_lower = [user.lower() for user in current_users]

msg = ''

for username in new_users:
    if username.lower() in current_users:
        msg = f"The {username.title()} already exists, You need another username."
    else:
        msg = f"The {username.title()} is not used."
    print(msg)
