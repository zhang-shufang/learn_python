class Restaurant:
    """A class about restaurant."""
    def __init__(self, restaurant_name, cuisine_type, 
            number_served=0):
        """Init attribution of name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Print the summary of the restaurant."""
        msg = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
        print(msg)

    def open_restaurant(self):
        """Print the restaurant is oponing."""
        print(f"{self.restaurant_name} is opening.")

    def set_number_served(self, number):
        """Set the number of people the restaurant served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increasse the number of diners."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """A class about ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize the ice cream stand."""
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = ['bluebrew', 'chocolate', 'vanilla', 'tea']

    def print_menu(self):
        """Display the ice cream flavor."""
        print("They have these ice cream:")
        for item in self.flavors:
            print(item)


dq = IceCreamStand('DQ', 'ice cream')
dq.describe_restaurant()
dq.print_menu()

# 注意特殊性可以在初始化时直接默认。
"""
    def __init__(self, name, cuisine_type='ice cream'):
        # Initialize an ice cream stand.
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        # Display the flavors available.
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
"""