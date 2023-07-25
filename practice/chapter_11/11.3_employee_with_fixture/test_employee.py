import pytest 
from employee import Employee


@pytest.fixture
def employee():
    """A example of employee class for all testing."""
    employee = Employee('zhang', 'sang', 1_5000)
    return employee

def test_give_default_raise(employee):
    """Test if give raise function of employee is working by default."""
    test_info = employee.give_raise()
    assert test_info == 2_0000

def test_give_custom_raise(employee):
    """Test if give raise function of employee is working with input."""
    test_info = employee.give_raise(1_0000)
    assert test_info == 2_5000