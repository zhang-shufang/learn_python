from random import randint

class Die:
    """一个关于骰子的类"""

    def __init__(self, num_side=6) -> None:
        """默认骰子是6面的"""
        self.num_sides = num_side

    def roll(self):
        """返回1到骰子面数之间的一个数字"""
        result = randint(1, self.num_sides)
        return result