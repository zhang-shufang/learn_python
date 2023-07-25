from pathlib import Path
import json

file = Path("favorite_number.json")

number = json.loads(file.read_text())

print(number)