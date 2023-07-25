from random import choice

numbers = [str(i) for i in range(10)]
char = ['a', 'c', 'd', 'e', 'g']

lottery = ''

for time in range(4):
    lottery += choice(numbers + char) + ' '

print("You will get the reward if you have these number:")
print(lottery)

# 做了不重复
"""
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a
#   while loop.
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
"""