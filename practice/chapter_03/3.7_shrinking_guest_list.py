# Invite people
guests = ['father', 'mother', 'grandpa']
for guest in guests:
    msg = f'{guest.title()}, please come to dinner'
    print(msg)

# Someone can't come, and we change to invite another one.
print(f"{guests[0].title()} can't come to dinner.")
guests[0] = 'tony'

for guest in guests:
    msg = f'{guest.title()}, please come to dinner'
    print(msg)

# We find a bigger table, so we can invite more people to dinner.
print("\nWe got a bigger table!")
guests.insert(0,'tom')
guests.insert(2,'jerry')
guests.append('eric')

for guest in guests:
    msg = f'{guest.title()}, please come to dinner'
    print(msg)

# Our new table won't arrive in time, so we need to shrink guests down to 2.
print('\nOur new table won\'t arrive in time, so we need to shrink guests down to 2.')

print(f'{guests.pop().title()}, I\'m sorry you can\'t come to dinner')
print(f'{guests.pop().title()}, I\'m sorry you can\'t come to dinner')
print(f'{guests.pop().title()}, I\'m sorry you can\'t come to dinner')
print(f'{guests.pop().title()}, I\'m sorry you can\'t come to dinner')
print(f'{guests[0].title()}, welcome to dinner')
print(f'{guests[1].title()}, welcome to dinner')

del guests[0]
del guests[0]

print(guests)