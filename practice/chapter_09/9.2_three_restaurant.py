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
kfc = Restaurant('KFC', 'fried chicken')
burgerking = Restaurant('Berger King', 'Hamburger')

laohongxing.describe_restaurant()

kfc.describe_restaurant()

burgerking.describe_restaurant()


# 注意增加对函数的描述
"""

"""