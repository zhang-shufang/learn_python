input_state = True

while input_state:
    pizza_topping = input("What pizza topping would you like? ")
    if pizza_topping == "quit":
        input_state = False
        break
    else:
        print(f"I'll add {pizza_topping} to your pizza.")
    
"""参考答案
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
"""