from pathlib import Path

print("---- Reading file ----")
path = Path('practice/chapter_10/learning_python.txt')
contents = path.read_text()

contents = contents.replace("Python", "C")      # 注意replace()并不改变本来的字符串，而是会返回一个改变后的字符串。

print(contents)
