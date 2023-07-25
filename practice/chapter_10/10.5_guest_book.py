from pathlib import Path


names = ""
prompt_name = "\nWhat is your name? "
prompt_quit = "\nFinish inputting? yes/no. "

while True:
    name = input(prompt_name)
    print(f"\nWelcome! {name.title()}.")
    names += name + "\n"

    if input(prompt_quit) == 'yes':
        break    
    
path = Path('guest_book.txt')
path.write_text(names)

# 注意用列表来收集用户的输入
"""
guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)
"""