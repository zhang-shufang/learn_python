from random import choice

numbers = [str(i) for i in range(10)]
chars = ['a', 'c', 'd', 'e', 'g']

possible = numbers + chars

my_ticket = ['2', '1', 'c', 'd']

draw_time = 0

print(my_ticket)
while my_ticket:
    current_draw = choice(possible)
    draw_time += 1
    print(draw_time)

    if current_draw == my_ticket[0]:
        my_ticket.pop(0)
        print(my_ticket)

print(f"You winning the ticket with {draw_time} times drawing.")