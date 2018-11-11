from dice import *

class Set: #a collection of dice
    dice = []
    def __init__(self):
        self.dice = [Dice() for x in range(5)]
        for die in self.dice:
            die.roll()
        self.sort()

    def setValues(self, values):
        for x in len(self.dice):
            self.dice[x].value = values[x]

    def hold(self, actions):
        if not len(self.dice) == len(actions):
            raise ValueError("Inconsistent length")
        for x in range(len(self.dice)):
            if actions[x]: self.dice[x].hold()

    def rollAll(self):
        for die in self.dice:
            if not die.fixed: die.roll()
        self.sort()

    def __repr__(self):
        return ", ".join([str(dice) for dice in self.dice])

    def sort(self):
        self.dice.sort(key=lambda x: x.value)
