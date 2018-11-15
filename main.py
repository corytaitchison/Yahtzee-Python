from dice import *
from set import *
from scores import *
from outcomes import *
from scorecard import *
from computerRun import Computer
from randomRun import RandomComputer

computerPlay = True #Player or computer
randomPlay = False #Random computer
doPrint = False #prints out dice rolls etc. (turn on if player)
doWrite = True #writes computer output to file

possibles = {} #possible choices left

def responseToInt(response):
    if response.lower() == "y":
        return True
    return False

def reroll(diceSet, computer = None, rolls2 = True):
    #Gets input as to which to hold, then rolls the rest and prints
    if computerPlay:
        count = [0, 0, 0, 0, 0, 0, 0]
        for x in diceSet.dice:
            count[x.value] += 1 #converts the dice values to a count
        computer.calculateChoice(count, possibles, rolls2) #calculates which to hold
        buffer = str(computer.action) #computer.action is initially a string e.g. "0100011" which means reroll 1 "1", 1 "5" and 1 "6" dice
        actions = []
        if not buffer: buffer = [0, 0, 0, 0, 0, 0, 0] #if buffer is empty, hold none
        for x in diceSet.dice:
            actions.append(not int(buffer[x.value])) #convert buffer to input actions y/n
    else:
        actions = [responseToInt(input("[{}] Fix? y/n ".format(diceSet.dice[x].value))) for x in range(len(diceSet.dice))]
    diceSet.hold(actions) #holds the requested dice
    diceSet.rollAll() #rolls the rest
    if doPrint: print(diceSet)

def turn(scorecard, computer = None):
    diceSet = Set() #Gets new set of dice
    if doPrint: print(diceSet)
    reroll(diceSet, computer, True) #roll1
    reroll(diceSet, computer, False) #roll2
    score = Score(diceSet.dice, possibles) #gets all possible scores from this roll
    if doPrint:
        if score.outcomes:
            print(score) #if scores are available
        else:
            print(": 0, ".join([x for x in possibles if possibles[x] > -1])) #if all scores are 0
    action = computer.chooseScore(score, possibles) if computer else input("Which score? ") #chooses which score to select
    try:
        scorecard.addScore(action, score.outcomes[action].score) #if exists, then add points
    except KeyError:
        scorecard.addScore(action, 0) #else add 0 points
    possibles[action] = -2 #cannot choose this score option again this game
    if doPrint: print(scorecard)
    if not any(possibles[x] > -1 for x in possibles): return False #if no more possible score options, then quit the loop
    return True #else go to next round

if __name__ == "__main__":
    if doWrite:
        file = open("computerResults.txt", "w")
        output = []
    for x in range(10): #amount of games to play
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
        computer = RandomComputer() if randomPlay else Computer(7.50*0.40, 1.80, 20.0*0.475, 0.35)
        while loop:
            if computerPlay:
                loop = turn(scorecard, computer)
            else:
                loop = turn(scorecard, None)
        if doWrite:
            output += [str(scorecard.total)]
            print(".", end = "", flush = True)
        if computerPlay and not doPrint and not doWrite: print(scorecard)
        if not doWrite: print("GAME OVER: Total score = " + str(scorecard.total))
    if doWrite:
        print("")
        output = ", ".join(output)
        file.write(output)
