from dice import *
from set import *
from scores import *
from outcomes import *
from scorecard import *
from computerRun import Computer
from sys import stdout

computerPlay = True #Player or computer
doPrint = False #prints out dice rolls etc. (turn on if player)

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

def reroll(diceSet, computer = None, rolls2 = True):
    #Gets input as to which to hold, then rolls the rest and prints
    if computerPlay:
        count = [0, 0, 0, 0, 0, 0, 0]
        for x in diceSet.dice:
            count[x.value] += 1
        computer.calculateChoice(count, possibles, rolls2)
        buffer = str(computer.action)
        actions = []
        if not buffer: buffer = [0, 0, 0, 0, 0, 0, 0]
        for x in diceSet.dice:
            actions.append(not int(buffer[x.value]))
    else:
        actions = [responseToInt(raw_input("[{}] Fix? y/n ".format( diceSet.dice[x].value))) for x in range(len(diceSet.dice))]
    diceSet.hold(actions)
    diceSet.rollAll()
    if doPrint: print(diceSet)

def turn(scorecard, computer = None):
    diceSet = Set() #Gets new set of dice
    if doPrint: print(diceSet)
    reroll(diceSet, computer, True)
    reroll(diceSet, computer, False)
    score = Score(diceSet.dice, possibles)
    if doPrint:
        if score.outcomes:
            print(score)
        else:
            print(": 0, ".join([x for x in possibles if possibles[x] > -1]))
    if computer:
        if score.outcomes:
            action, foo = score.getHighestScore()
        else:
            action = [x for x in possibles if possibles[x] > -1][0]
    else:
        action = raw_input("Which score? ")
    try:
        scorecard.addScore(action, score.outcomes[action].score)
    except KeyError:
        scorecard.addScore(action, 0)
    possibles[action] = -2
    if doPrint: print(scorecard)
    if not any(possibles[x] > -1 for x in possibles): return False
    return True

if __name__ == "__main__":
    file = open("computerResults.txt", "w")
    output = []
    for x in range(200):
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
        scorecard = Scorecard()
        loop = True
        computer = Computer()
        while loop:
            if computerPlay:
                loop = turn(scorecard, computer)
            else:
                loop = turn(scorecard, None)
        output += [str(scorecard.total)]
        stdout.write(".")
        stdout.flush()
        #print(scorecard)
        #print("GAME OVER: Total score = " + str(scorecard.total))
    print("")
    output = ", ".join(output)
    file.write(output)
