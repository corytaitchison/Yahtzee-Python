from outcomes import *
from copy import deepcopy

def check(array, val, operator=">="):
    return eval("[x for x in array if x {} val]".format(operator))

def checkStraight(array): #converts array to a binary string
    output = []
    for x in array:
        if x != 0:
            output.append("1")
        else:
            output.append("0")
    return "".join(output) #e.g. [0,1,5,0,3] --> 01101

class Score: #outputs all possible non-zero scores for a given dice set
    dice = []
    count = [0, 0, 0, 0, 0, 0, 0]
    fits = {}
    outcomes = {}

    def match(self):
        count = self.count
        for x in range(1,7): #does uppers
            if count[x] > 0: self.fits["upper" + str(x)] += 1
        if check(count, 3): self.fits["three"] += 1
        if check(count, 4): self.fits["four"] += 1
        if check(count, 3, "==") and check(count, 2, "=="): self.fits["fullHouse"] += 1
        if check(count, 5): self.fits["yahtzee"] += 1
        if "1111" in checkStraight(count): self.fits["sStraight"] += 1
        if "11111" in checkStraight(count): self.fits["lStraight"] += 1

    def __init__(self, arg, fits): #arg is the dice set
        self.dice = [x.value for x in arg] #takes the value for each dice
        self.fits = deepcopy(fits)
        self.count = [0, 0, 0, 0, 0, 0, 0]
        self.outcomes = {}
        for x in self.dice:
            self.count[x] += 1 #creates a count i.e. if count[1]=3, then there are three ones in the dice set
        #print(", ".join(["[{}]: {}".format(x, self.count[x]) for x in range(1,7)]))
        self.match()
        for key in self.fits:
            if self.fits[key] > 0:
                type = key[:-1] if "upper" in key else key
                variant = int(key[-1:]) if "upper" in key else 0
                self.outcomes[key] = Outcome(type, variant, self.dice)

    def __repr__(self):
        return ", ".join(["{}({}): {}".format(self.outcomes[x].type, self.outcomes[x].variant, self.outcomes[x].score) for x in self.outcomes])
