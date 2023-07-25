prompt = "\nPlease enter your age and I will tell you the ticket price. "
prompt += "\nOr enter 'quit' to finish this inquiring. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("You are free for the movie.")
        elif age >= 3 and age < 12:
            print("You need pay 10 dollars for the movie.")
        elif age >=12:
            print("You need pay 15 dollars for the movie.")
    