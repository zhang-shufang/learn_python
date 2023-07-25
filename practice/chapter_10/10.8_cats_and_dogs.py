from pathlib import Path

pathes = {
    'cats': Path("practice/chapter_10/cats.txt"),
    'dogs': Path("practice/chapter_10/dogs.txt")}
contents = {}

for name, path in pathes.items():
    try:
        contents[name] = path.read_text()
    except FileNotFoundError:
        print(f"{path} file is not in there.")

for name, items in contents.items():
    print(f"\n{name.title()} include:")
    print(items)
