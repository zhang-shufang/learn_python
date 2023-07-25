from random import randint

class Die:
    """A class about die"""
    def __init__(self, side=6):
        """Initialize"""
        self.side = side

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.side)

print("\nRoll six sides die ten times.")    
die_6 = Die()
for time in range(10):
    print(die_6.roll_die())

print("\nRoll ten sides die ten times.")
die_10 = Die(10)
for time in range(10):
    print(die_10.roll_die())

print("\nRoll twenty sides die ten times.")
die_20 = Die(20)
for time in range(10):
    print(die_20.roll_die())

# 注意把结果储存起来
"""
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
"""