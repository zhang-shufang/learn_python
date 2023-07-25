class User:
    """A class about users."""
    def __init__(self, first_name, last_name, login_attermpts=0):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attermpts = login_attermpts

    def describe_user(self):
        """Print user informations."""
        print(f"first name: {self.first_name.title()}")
        print(f"last name: {self.last_name.title()}")

    def greet_user(self):
        """Greet user."""
        user_name = self.first_name.title() + " " + self.last_name.title()
        print(f"Greeting!, {user_name}")

    def increment_login_attempts(self):
        """Increase the login time when user is trying to login."""
        self.login_attermpts += 1
    
    def reset_login_attempts(self):
        """Allow to set the login attermpts to 0."""
        self.login_attermpts = 0

user1 = User('zhang', 'shufang')


for counter in range(10):
    user1.increment_login_attempts()
    print("User login attermpt.")
print(user1.login_attermpts)

print("\nReset the login attempts.")
user1.reset_login_attempts()
print(user1.login_attermpts)

# 注意构造函数部分，不需要初始化的可以不定义形参。
"""
def __init__(self, first_name, last_name, username, email, location):
        # Initialize the user.
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
"""