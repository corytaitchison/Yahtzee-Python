class Scorecard:
    scores = {
        "upper1": 0,
        "upper2": 0,
        "upper3": 0,
        "upper4": 0,
        "upper5": 0,
        "upper6": 0,
        "upperBonus": 0,
        "three": 0,
        "four": 0,
        "fullHouse": 0,
        "sStraight": 0,
        "lStraight": 0,
        "yahtzee": 0,
        "chance": 0,
        "yahtzeeBonus": 0,
    }
    upperTotal = 0
    lowerTotal = 0
    total = 0
    def __init__(self):
        pass

    def addScore(self, id, score):
        self.scores[id] = score;
        if self.upperTotal >= 63: self.scores["upperBonus"] = 35
        self.upperTotal = sum([self.scores[x] for x in self.scores if "upper" in x])
        self.lowerTotal = sum([self.scores[x] for x in self.scores if not "upper" in x])
        self.total = self.upperTotal + self.lowerTotal

    def __repr__(self):
        return "\
        ~~~SCORE CARD~~~\n\
        Aces: {}    Twos: {}\n\
        Threes: {}  Fours: {}\n\
        Fives: {}   Sixes: {}\n\
        Bonus: {}\n\
        Upper Total: {}\n\
        \n\
        3 of a kind: {}\n\
        4 of a kind: {}\n\
        Full House: {}\n\
        Sm Straight: {}\n\
        Lg Straight: {}\n\
        Yahtzee: {}\n\
        Chance: {}\n\
        Lower Total: {}\n\
        TOTAL: {}\n\
        ~~~~~~~~~~~~~~~~".format(self.scores["upper1"], self.scores["upper2"], self.scores["upper3"], self.scores["upper4"], self.scores["upper5"], self.scores["upper6"], self.scores["upperBonus"], self.upperTotal, self.scores["three"], self.scores["four"], self.scores["fullHouse"], self.scores["sStraight"], self.scores["lStraight"], self.scores["yahtzee"], self.scores["chance"], self.lowerTotal, self.lowerTotal + self.upperTotal)
