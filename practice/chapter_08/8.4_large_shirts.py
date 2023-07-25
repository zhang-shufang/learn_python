def make_t_shirt(size='L', text='I love Python'):
    """Print the T-shirt's size and printing text"""
    msg = f"This T-shirt has '{text}' text and it is {size} size."
    print(msg)

make_t_shirt('L')

make_t_shirt(size='M')

make_t_shirt(text='Good')

"""reference
def make_shirt(size, message):
    # Summarize the shirt that's going to be made.
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
"""