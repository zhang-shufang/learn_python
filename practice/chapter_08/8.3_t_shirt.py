def make_t_shirt(size, text):
    """Print the T-shirt's size and printing text"""
    msg = f"This T-shirt has '{text}' text and it is {size} size."
    print(msg)

make_t_shirt('M', 'Good')

make_t_shirt(size='S', text='Bad')

"""reference
def make_shirt(size, message):
    # Summarize the shirt that's going to be made.
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
"""