import computerRun
import random

class RandomComputer(computerRun.Computer):
    def __init__(self):
        self.choices = {}
        self.action = ""

    def calculateChoice(self, current, possibles, rolls2 = True):
        self.action = "".join([str(x) for x in current])

    def chooseScore(self, score, possibles):
        if score.outcomes:
            x = list(score.outcomes)[random.randrange(0,len(score.outcomes))]
            foo = score.outcomes[x].type + str(score.outcomes[x].variant) if score.outcomes[x].variant != 0 else score.outcomes[x].type
        else:
            foo = [x for x in possibles if possibles[x] > -1][0]
        return foo
