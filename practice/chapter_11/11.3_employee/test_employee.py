from employee import Employee


def test_give_default_raise():
    """Test if give raise function of employee is working by default."""
    employee = Employee('zhang', 'sang', 1_5000)
    test_info = employee.give_raise()
    assert test_info == 2_0000

def test_give_custom_raise():
    """Test if give raise function of employee is working with input."""
    employee = Employee('zhang', 'sang', 1_5000)
    test_info = employee.give_raise(1_0000)
    assert test_info == 2_5000

# 注意可以直接访问类的属性，不一定需要返回值。
"""
def test_give_default_raise():
    employee = Employee('zhang', 'sang', 1_5000)
    employee.give_raise()
    assert employee.annual_salary == 2_0000

def test_give_custom_raise():
    employee = Employee('zhang', 'sang', 1_5000)
    employee.give_raise(1_0000)
    assert employee.annual_salary == 2_5000
"""