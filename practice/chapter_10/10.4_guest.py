from pathlib import Path


contents = input("What is your name? ")

path = Path('guest.txt')
path.write_text(contents)

print(f"Welcome! {contents.title()}.")
