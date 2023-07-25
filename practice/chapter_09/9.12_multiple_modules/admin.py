"""A collection of classes for modeling admins."""

from user import User

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
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"]
    
    def show_privileges(self):
        """Display all the privileges admin has."""
        for item in self.privileges:
            print(item)