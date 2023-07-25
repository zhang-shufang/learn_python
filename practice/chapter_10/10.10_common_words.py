from pathlib import Path

file = Path("practice/chapter_10/moby_dick.txt")

contents = file.read_text()

num_the1 = contents.lower().count("the")
num_the2 = contents.lower().count("the ")

print(num_the1)
print(num_the2)


# 注意用了一个函数，主要是因为用了try然后需要用函数吧。
"""
from pathlib import Path

def count_common_words(filename, word):
    # Count how many times word appears in the text.
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')
"""