guests = ['father', 'mother', 'grandpa']
for guest in guests:
    msg = f'{guest.title()}, please come to dinner'
    print(msg)

print(f"{guests[0].title()} can't come to dinner.")

guests[0] = 'tony'

for guest in guests:
    msg = f'{guest.title()}, please come to dinner'
    print(msg)