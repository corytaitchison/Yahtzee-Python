import random
class Dice:
    value = 0
    fixed = 0
    def __init__(self, value=0):
        self.value = value
        self.fixed = 0

    def roll(self):
        self.value = random.randrange(1,7)

    def __repr__(self):
        return "[" + str(self.value) + "]"

    def hold(self):
        self.fixed = True
