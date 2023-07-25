"""A collection of classes for modeling users."""

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


class Admin(User):
    """A class about admin."""
    def __init__(self, first_name, last_name, login_attermpts=0):
        """Initialize the admin."""
        super().__init__(first_name, last_name, login_attermpts)
        self.privileges = Privileges()


class Privileges:
    """A class about privileges."""
    def __init__(self):
        """Initialize."""
        self.privileges = []
    
    def show_privileges(self):
        """Display all the privileges admin has."""
        for item in self.privileges:
            print(item)