from dice import *
from set import *
from scores import *
from outcomes import *
from scorecard import *

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

def responseToInt(response):
    if response.lower() == "y":
        return True
    return False

def reroll(diceSet):
    #Gets input as to which to hold, then rolls the rest and prints
    actions = [responseToInt(raw_input("[{}] Fix? y/n ".format( diceSet.dice[x].value))) for x in range(len(diceSet.dice))]
    diceSet.hold(actions)
    diceSet.rollAll()
    print(diceSet)

def turn(scorecard):
    diceSet = Set() #Gets new set of dice
    print(diceSet)
    reroll(diceSet)
    reroll(diceSet)
    score = Score(diceSet.dice, possibles)
    if score.outcomes:
        print(score)
    else:
        print(": 0, ".join([x for x in possibles if possibles[x] > -1]))
    action = raw_input("Which score? ")
    try:
        scorecard.addScore(action, score.outcomes[action].score)
    except KeyError:
        scorecard.addScore(action, 0)
    possibles[action] = -2
    print(scorecard)
    if not any(possibles[x] > -1 for x in possibles): return False
    return True

if __name__ == "__main__":
    scorecard = Scorecard()
    loop = True
    while loop:
        loop = turn(scorecard)
    print("GAME OVER: Total score = " + str(scorecard.total))
