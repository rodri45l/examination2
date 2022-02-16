from random import randint


class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turnScore = 0


    def sumTurnScore(self):
        self.score += self.turnScore
        self.turnScore = 0


class Dice():

    def __init__(self):
        self.roll = 0

    def rollDice(self):
        self.roll = randint(1, 6)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'