usernames = ['designer', 'programer', 'admin', 'PM', 'boss']
msg = ''
for username in usernames:
    if username == 'admin':
        msg = f"Hello {username}, would you like to see a status report?"
    else:
        msg = f"Hello {username}, thank you for logging in again."
    print(msg)
