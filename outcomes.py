from dice import *

class Outcome: #converts the outcome to a score
    type = ""
    score = 0
    variant = 0
    dice = []
    def __init__(self, type, variant, dice):
        self.type = type
        self.dice = dice
        self.variant = variant
        self.score = eval("self." + type + "()")

    def upper(self):
        return sum([x for x in self.dice if x == self.variant])

    def three(self):
        return sum(self.dice)

    def four(self):
        return sum(self.dice)

    def fullHouse(self):
        return 25

    def sStraight(self):
        return 30

    def lStraight(self):
        return 40

    def yahtzee(self):
        return 50

    def chance(self):
        return sum(self.dice)
