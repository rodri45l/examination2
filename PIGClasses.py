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

    def rollDice(self, PrintDice):
        diceFaceDic = {1: '~Y?77777777777777?Y~\n\
#^                :#\
\n#.                .#\
\n#.      ^7?~.     .#\
\n#.     ^@@@@7     .#\
\n#.      ^??~.     .#\
\n#.                .#\
\n#:                :#\
\n~Y?77777777777777?Y!',
                       2: '^.:!7^............:^\
\n^:#@@@?            ^\
\n^.P&&B!            ^\
\n^  ..              ^\
\n^                  ^\
\n^              ..  ^\
\n^            !B&&P.^\
\n^            ?@@@#:^\
\n^:............^7!:.^',
                       3: '^:............^!!:.^\n\
^            ?@@@#:^\n\
^            !B&&P.^\n\
^      .7557.  ..  ^\n\
^      7@@@@7      ^\n\
^  ..  .7557.      ^\n\
^.P&&B!            ^\n\
^:#@@@?            ^\n\
^.:!!^............:^',
                       4: '.:^::::::::::::::::.\n\
^:.75Y^      :J5?::^\n\
~ ^@@@P      ?@@@? ~\n\
~  ^7!.      .~7~  ~\n\
~                  ~\n\
~                  ~\n\
~  ~J?:      .7J7. ~\n\
~ ^@@@G      J@@@? ~\n\
^: ~J?:      .7J7.:~\n\
.:^::::::::::::::::.',
                       5: '^.:!!^........^!!:.^\n\
^:#@@@?      ?@@@#:^\n\
^.P&&B!      !B&&P.^\n\
^  ..  .7557.  ..  ^\n\
^      7@@@@7      ^\n\
^  ..  .7557.  ..  ^\n\
^.P&&B!      !B&&P.^\n\
^:#@@@?      ?@@@#:^\n\
^.:!!^........^!!:.^',
                       6: '^##################^\n\
^.B@@@J &@@& J@@@B.^\n\
^.P&&#7 B&&G 7#&#5.^\n\
^  ..    ..    ..  ^\n\
^                  ^\n\
^  ..    ..    ..  ^\n\
^.P&&#7 B&&G 7#&#5.^\n\
^.B@@@J &@@& J@@@B.^\n\
####################',
                       }

        self.roll = randint(1, 6)
        if PrintDice:
            print(diceFaceDic[self.roll] + '\n')


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
    NOT_UNDERLINED = '\033[24m'
    RESET = '\u001b[0m'
