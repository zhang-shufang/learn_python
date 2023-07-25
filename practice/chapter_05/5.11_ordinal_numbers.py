list = [number for number in range(1, 10)]
# number = list(range(1, 10))
# print(list)

msg = ''

for number in list:
    if number == 1:
        msg = f"{number}st"
    elif number == 2:
        msg = f"{number}nd"
    elif number == 3:
        msg = f"{number}rd"
    elif number >= 4 and number < 10:
        msg = f"{number}th"   
    print(msg)