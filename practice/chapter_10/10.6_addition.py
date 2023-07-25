try:
    a = int(input("\nPlease enter the number to add: "))
    b = int(input("Please enter another number to add: "))
except ValueError:
    print("Only number can be accepted. ")
else:
    print(f"The result is {a+b}.")