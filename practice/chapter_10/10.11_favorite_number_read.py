from pathlib import Path
import json

file = Path("favorite_number.json")

favorite_number = input("Please enter your favorite number: ")

data_to_write = json.dumps(favorite_number)
file.write_text(data_to_write)