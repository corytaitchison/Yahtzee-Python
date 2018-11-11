from math import factorial, pow
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

class Computer:
    choices = {}
    combination = []

    def __init__(self):
        self.choices = {}
        file = open("combinations.txt", "r")
        self.combinations = file.read().split(", ")
        self.combinations = [[int(y) for y in x] for x in self.combinations]


if __name__ == "__main__":
    current = [0,0,0,0,0,1,5]
    computer = Computer()
    for goal in computer.combinations:
        diff = [goal[x] - current[x] for x in range(len(goal))]
        prob = 1.0
        rollYes = []
        for x in diff:
            if x < 0:
                rollYes.append(-1*x)
            else:
                rollYes.append(0)
        rollYes = "".join([str(x) for x in rollYes])
        for x in range(1,len(goal)):
            if diff[x] > 0:
                prob *= prob2(current[x], goal[x])
        try:
            computer.choices[rollYes] += prob
        except KeyError:
            computer.choices[rollYes] = prob
    print(computer.choices)
