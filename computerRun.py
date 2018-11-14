from math import factorial, pow, sqrt, erf
from scores import *
from set import *
from dice import *

def choose(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def prob1(p, q, n=5):
    c = choose(n-p, q-p)
    return c * pow(1.0/6.0, q-p) * pow(5.0/6.0, n-q)

def prob2(p, q, n=5):
    output = 0
    for i in range(p, q+1):
        output += prob1(p, i, n)*prob1(i, q, n)
    return output

class Computer(object):
    choices = {}
    combination = []
    action = ""

    def __init__(self):
        self.choices = {}
        file = open("combinations.txt", "r")
        self.combinations = file.read().split(", ")
        self.combinations = [[int(y) for y in x] for x in self.combinations]
        self.action = ""

    def weight(self, prob, highestScore):
        probNormal = 7.5
        scoreNormal = 20.0
        return (((prob-probNormal)/probNormal)+1) * (((highestScore-scoreNormal)/scoreNormal)+1) # TODO: Actually make this good (whats the best way to do this?)

    def chooseScore(self, score, possibles):
        if score.outcomes:
            foo, highestScore = score.getHighestScore() #choose the highest score
            ## TODO: Make this more complicated,not just the highest, but based on the probability of getting the remaining options maybe?
        else:
            foo = [x for x in possibles if possibles[x] > -1][0]
        return foo

    def calculateChoice(self, current, possibles, rolls2 = True): #calculates which to hold or reroll
        self.choices = {}
        for goal in self.combinations:
            diff = [goal[x] - current[x] for x in range(len(goal))]
            prob = 1.0
            rollYes = [] #Whether or not to roll for each dice by value (not count) e.g. 0002000 = roll 2 dices with value 3
            for x in diff:
                if x < 0:
                    rollYes.append(-1*x) #if difference = -2, make it 2 (i.e. roll 2 dice)
                else:
                    rollYes.append(0) #else don't roll
            rollYes = "".join([str(x) for x in rollYes])

            for x in range(1,len(goal)):
                if diff[x] > 0:
                    if rolls2:
                        prob *= prob2(current[x], goal[x]) #probability to get to goal count
                    else:
                        prob *= prob1(current[x], goal[x])

            score = Score(goal, possibles, True) #gets possible scores for the given goal
            highestScoreID, highestScore = score.getHighestScore() #gets highest score

            prob = self.weight(prob, highestScore)

            try:
                self.choices[rollYes] += prob
            except KeyError:
                self.choices[rollYes] = prob
        highestWeight = 0
        highestWeightID = ""
        for key in self.choices:
            if self.choices[key] > highestWeight:
                highestWeight = self.choices[key]
                highestWeightID = key
        self.action = highestWeightID

if __name__ == "__main__":
    possibles = {
        "upper1": 0,
        "upper2": 0,
        "upper3": 0,
        "upper4": 0,
        "upper5": 0,
        "upper6": 0,
        "three": 0,
        "four": 0,
        "fullHouse": 0,
        "sStraight": 0,
        "lStraight": 0,
        "yahtzee": 0,
        "chance": 1,
    }
    current = [0,0,0,1,1,0,3]
    computer = Computer()
    computer.calculateChoice(current, possibles, True)
    print(computer.choices)
    print(computer.action)
