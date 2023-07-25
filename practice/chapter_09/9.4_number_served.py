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

laohongxing = Restaurant('Laohongxing', 'shanghaicai')
print(laohongxing.number_served)

print("\nA day goes by.")
laohongxing.number_served = 100
print(laohongxing.number_served)

print("\nTwo days goes by.")
laohongxing.set_number_served(200)
print(laohongxing.number_served)

print("\nFour days goes by.")
laohongxing.increment_number_served(100)
print(laohongxing.number_served)

# 注意形参的命名和注释的写法
"""
    def set_number_served(self, number_served):
        # Allow user to set the number of customers that have been served.
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        # Allow user to increment the number of customers served.
        self.number_served += additional_served
"""