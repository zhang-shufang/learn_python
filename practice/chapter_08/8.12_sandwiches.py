def make_sandwiches(*ingredients):
    """Print all ingredients the sandwiche need."""
    print("\nThe sandwiche will includes:")
    for ingredient in ingredients:
        print(ingredient)

make_sandwiches('tomato', 'potato', 'chicken')

make_sandwiches('beef', 'onion', 'cheeze', 'lettuce')

# 注意英文表述和交互。
"""reference
def make_sandwich(*items):
    # Make a sandwich with the given items.
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
"""