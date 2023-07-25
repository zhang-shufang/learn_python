from pathlib import Path
import json

file = Path("favorite_number1.json")

if file.exists():
    number = json.loads(file.read_text())
    print(number)
else:
    favorite_number = input("Please enter your favorite number: ")

    data_to_write = json.dumps(favorite_number)
    file.write_text(data_to_write)

# 参考使用try的方法
"""
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
"""