name_prompt = "\nWhat is your name? "
vacation_prompt = "\nIf you could visit one place in the world, where yould you go? "

survey_state = True

# Responses will be stored in the form {name: place}.   **参考答案**
# responses = {}
vacation_dict = {}

while survey_state:
    name = input(name_prompt)
    if name == "finish":
        print("The survey is finished.")
        break
    else:
        vacation = input(vacation_prompt)
    vacation_dict[name] = vacation

for name, vacation in vacation_dict.items():
    print(f"{name.title()} would like to go to {vacation}.")

"""参考答案的点在于
1. 字典键值对的标注可以放在注视里。
2. 代码里的交互整体更友好。
"""

"""参考代码
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.   # **注意数据格式的标注方式**
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
"""