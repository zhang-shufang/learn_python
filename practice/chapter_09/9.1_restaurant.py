class Restaurant:
    """A class about restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Init attribution of name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
        print(msg)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening.")

laohongxing = Restaurant('Laohongxing', 'shanghaicai')
print(laohongxing.restaurant_name)
print(laohongxing.cuisine_type)


laohongxing.describe_restaurant()
laohongxing.open_restaurant()

# 注意增加对函数的描述
"""
class Restaurant:
    # A class representing a restaurant.

    def __init__(self, name, cuisine_type):
        # Initialize the restaurant.
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Display a summary of the restaurant.
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        # Display a message that the restaurant is open.
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
"""