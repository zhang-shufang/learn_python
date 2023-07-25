glossary = {'string': 'A series of characters.',
           'comment': 'A note in a program that Python interpreter ignores.',
           'list': 'A collection of items in a particular order.', 
           'loop': 'Work through a collection of items, one at a time.',
           'dictionary': 'A collection of key-value pairs.',
           }
for term in glossary:
    print(f'{term.title()}: {glossary[term]}')