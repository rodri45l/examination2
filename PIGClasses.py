from random import randint


class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turnScore = 0

    def setScore(self, score):
        self.score = score

    def addTurnScore(self, turnScore):
        self.turnScore += turnScore

    def resetTurnScore(self):
        self.turnScore = 0

    def sumTurnScore(self):
        self.score += self.turnScore

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getTurnScore(self):
        return self.turnScore


class Dice():

    def __init__(self):
        self.roll = 0

    def roll(self):
        self.roll = randint(1, 6)
        return self.roll
