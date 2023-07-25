from pathlib import Path

print("---- Reading file ----")
path = Path('practice/chapter_10/learning_python.txt')
contents = path.read_text()

print(contents)

print("\n---- Reading file in lines ----")
path = Path('practice/chapter_10/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

