import numpy as np
import main
from dice import *
from set import *
from scores import *
from outcomes import *
from scorecard import *
from computerRun import Computer

class NeuralNet:
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = np.array([[0.55, 1.85, 0.65, 0.5]]).T
        self.iterAmounts = np.array([0.5, 0.5, 0.5, 0.4])
        #self.synaptic_weights = 2 * np.random.random((4,1)) #values in range of 0-2
        self.synaptic_values = np.array([[7.50, 1.00, 20.00, 1.00]]).T

    def sigmoid(self, x):
        return 1/(1+np.exp(1-x))

    def sigmoidDerivative(self, x):
        return x*(1-x)

    def train(self, iterations, trainingRange = 10):
        for synapse in range(4):
            highScore = 185
            highestWeight = self.synaptic_weights[synapse][0]
            for iteration in range(iterations):
                output = 0.0
                for _iter in range(trainingRange):
                    scorecard = Scorecard()
                    inputs = self.synaptic_values * self.synaptic_weights
                    computer = Computer(inputs[0][0], inputs[1][0], inputs[2][0], inputs[3][0])
                    main.possibles = {
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
                    main.doPrint = False
                    loop = True
                    while loop:
                        loop = main.turn(scorecard, computer)
                    output += scorecard.total
                    print(".", end = "", flush=True)
                output /= trainingRange
                if output > highScore:
                    highestWeight = self.synaptic_weights[synapse][0]
                    highScore = output
                self.synaptic_weights[synapse][0] -= (self.iterAmounts / iterations)[synapse]
                print("{} {} ".format(output, ", ".join([str(x) for x in self.synaptic_weights])), end = " ", flush = True)
            self.synaptic_weights[synapse][0] = highestWeight
            print(" Highest = {}".format(", ".join([str(x) for x in self.synaptic_weights])))

if __name__ == "__main__":
    neuralNet = NeuralNet()
    neuralNet.train(20, 20)
