class Employee:
    """This class is about the information of employees."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, annual_salary_increment=5000):
        """Increase the employee's salary."""
        self.annual_salary += annual_salary_increment
        return self.annual_salary