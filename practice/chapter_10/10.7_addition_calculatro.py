print("Enter 'q' at any time to quit.\n")

x = y = 0

while True:
    if not x:
        current_input = input("\nPlease enter the number to add: ")
        if current_input == 'q':
            break
        try:
            x = int(current_input)
        except ValueError:
            print("Only number can be accepted. ")
    elif not y:
        current_input = input("Please enter another number to add: ")
        if current_input == 'q':
            break
        try:
            y = int(current_input)
        except ValueError:
            print("Only number can be accepted. ")

    if x and y:
        print(f"{x} sums {y} is {x + y}.")
        break


# 我的方法更好一些，注意他可以随时退出的功能。

"""
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
"""