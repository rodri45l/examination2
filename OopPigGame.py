from PIGClasses import Player as p
from PIGClasses import Dice as d
from PIGClasses import bcolors as LetCol

GOAL = 100
DIVIDER = "===================================================================\
======================================="


def printWelcomeMessage():
    print(f'{LetCol.HEADER}{DIVIDER}')
    print(f'{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG\
{LetCol.NOT_UNDERLINED}')
    print(f'{LetCol.OKCYAN}In this game wins the first player to reach 100 points')
    print(f'{LetCol.OKCYAN}Players take turns to roll a single dice as many times\
as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.')
    print(f'{LetCol.HEADER}{DIVIDER}')


def showMenu():
    print(f'{LetCol.UNDERLINE}{ LetCol.OKCYAN}Press 1 to play vs the computer.')
    print(f'Press 2 for 2 players.{LetCol.NOT_UNDERLINED}')
    choice = [1, 2]
    option = 0
    while(option not in choice):
        try:
            option = int(input(f'{LetCol.OKCYAN}Please input 1 or 2 \
depending on your choice: {LetCol.RESET}'))
        except ValueError:
            print(f'{LetCol.FAIL} Please enter a valid value (1, 2)')
            print('\n')
    return option


def showOptionMenu():
    print('Enter 1 to roll the dice')
    print('Enter 2 to hold your score')
    option2 = int(input(f'Enter your choice: {LetCol.RESET}'))
    return option2


def createPlayer(n):
    player = p(input(f"{LetCol.OKCYAN}Please Player{n} enter your name: {LetCol.RESET}"))
    return player


def playerVsMachine():
    player = createPlayer(1)
    computer = p("Computer")
    keepRunning = True
    while(keepRunning):
        player = playerTurn(player)
        if(player.score >= GOAL):
            print(f'{LetCol.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{LetCol.RESET}')
            print(f'{DIVIDER}')
            keepRunning = False
        computer = computerTurn(computer)
        if(computer.score >= GOAL):
            print(f'{c.FAIL}You lose, computers > humans')
            keepRunning = False
    print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")


def playerTurn(player):
    option = 0
    keepRunning = True
    x = d()
    while(keepRunning):
        print(f'{LetCol.HEADER}{DIVIDER}')
        print(f'{LetCol.UNDERLINE}Please {player.name} choose:{LetCol.NOT_UNDERLINED}')
        option = showOptionMenu()
        if (option == 2):
            keepRunning = False
        elif(option == 1):
            x.rollDice(True)

            if(x.roll == 1):
                player.turnScore = 0
                print(f"{LetCol.WARNING}Unlucky, you scored a 1")
                print(f"{LetCol.OKBLUE}Your score this turn is {player.turnScore}")
                print(f"{player.name}'s Total score this turn is \
{player.score}")
                return player
            else:
                print(f"You got a {x.roll}")
                player.turnScore += x.roll
                print(f'{LetCol.OKBLUE}Your score for this turn is:\
 {player.turnScore}')
        else:
            print(f'{LetCol.FAIL}!!!!!!\nPlease enter a valid option\n!!!!!!')
            playerTurn(player)
    print(f"{LetCol.OKBLUE}Your score this turn is {player.turnScore}")
    player.sumTurnScore()
    print(f"{player.name}'s Total score this turn is {player.score}")

    return player


def computerTurn(computer):
    dice = d()
    while(computer.turnScore < 20):
        dice.rollDice(False)
        if(dice.roll == 1):
            computer.turnScore = 0
            print(f"Computer score this turn is {computer.score}")
            return computer
        else:
            computer.turnScore += dice.roll
    print(f"Computer score this turn is {computer.turnScore}")
    computer.sumTurnScore()
    print(f"Computer Total score is {computer.score}")
    return computer


def playerVsPlayer():
    player1 = createPlayer(1)
    player2 = createPlayer(2)
    keepRunning = True
    while(keepRunning):
        print(DIVIDER)
        print(f"{player1.name} It's Your turn!")
        print(DIVIDER)
        player1 = playerTurn(player1)
        if(player1.score >= GOAL):
            print(f'{LetCol.OKGREEN} CONGRATULATIONS {player1.name}\
 YOU WIN!!{LetCol.RESET}')
            keepRunning = False
            break
        print(DIVIDER)
        print(f"{player2.name} It's Your turn!")
        print(DIVIDER)
        player2 = playerTurn(player2)
        if(player2.score >= GOAL):
            print(f'{LetCol.OKGREEN} CONGRATULATIONS {player2.name} YOU WIN!!\
{LetCol.RESET}')
            keepRunning = False
            break
    print(f"Final Score:\n{player1.name}: {player1.score}\n\
{player2.name}: {player2.score}")


def main():
    printWelcomeMessage()
    playersOPtion = showMenu()
    if playersOPtion == 1:
        playerVsMachine()
    else:
        playerVsPlayer()


if __name__ == '__main__':
    main()
