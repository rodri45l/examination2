from PIGClasses import Player as p
from PIGClasses import Dice as d
from PIGClasses import bcolors as LetCol
import ShouldRoll as prob

GOAL = 100
DIVIDER = "===================================================================\
======================================="


def printWelcomeMessage():
    print(f'{LetCol.HEADER}{DIVIDER}\n\
{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG\n\
{LetCol.NOT_UNDERLINED}{LetCol.OKCYAN}In this game wins the first player to \
reach 100 points{LetCol.OKCYAN}\n\
Players take turns to roll a single dice as many times\
 as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.\n{LetCol.HEADER}{DIVIDER}')


def showMenu():
    print(f'{LetCol.UNDERLINE}{ LetCol.OKCYAN}Press 1\
 to play vs the computer.')
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
    player = p(input(f"{LetCol.OKCYAN}Please Player{n} \
enter your name: {LetCol.RESET}"))
    return player


def playerVsMachine():
    player = createPlayer(1)
    computer = p("Computer")
    while(player.score < 100 and computer.score < 100):
        player = playerTurn(player)
        if(player.score >= 100):
            break
        computer = computerTurn(computer, player)
        if(computer.score >= 100):
            break
        print(f'Your probabilities to win are: \
{prob.pWin(player.score, computer.score, 0):.2f}')

    if(player.score >= GOAL):
        print(f'{LetCol.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{LetCol.RESET}')
        print(f'{DIVIDER}')
    elif(computer.score >= GOAL):
        print(f'{LetCol.FAIL}You lose, computers > humans')
        print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")


def playerTurn(player):
    option = 0
    keepRunning = True
    x = d()
    while(keepRunning):
        print(f'{LetCol.HEADER}{DIVIDER}\n\
{LetCol.UNDERLINE}Please {player.name} choose:{LetCol.NOT_UNDERLINED}')
        option = showOptionMenu()
        if (option == 2):
            keepRunning = False
        elif(option == 1):
            x.rollDice(True)

            if(x.roll == 1):
                player.turnScore = 0
                print(f"{LetCol.WARNING}Unlucky, you scored a 1\n\
{LetCol.OKBLUE}Your score this turn is {player.turnScore}\n\
{player.name}'s Total score this turn is \
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


def computerTurn(computer, player):
    dice = d()
    while(prob.shouldRoll(computer.score, player.score, computer.turnScore)):
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
    while(player1.score < 100 and player2.score < 100):
        print(f"{DIVIDER}\n{player1.name} It's Your turn!\n{DIVIDER}")
        player1 = playerTurn(player1)
        print(f"{DIVIDER}\n{player2.name} It's Your turn!\n{DIVIDER}")
        player2 = playerTurn(player2)
        print(f'{DIVIDER}\nProbabilites to win:\n{player1.name}: \
{prob.pWin(player1.score, player2.score, 0):.2f}\n{player2.name}: \
{prob.pWin(player2.score, player1.score, 0):.2f}\n{DIVIDER}')
    if(player1.score >= GOAL):
        print(f'{LetCol.OKGREEN} CONGRATULATIONS {player1.name}\
 YOU WIN!!{LetCol.RESET}')

    elif(player2.score >= GOAL):
        print(f'{LetCol.OKGREEN} CONGRATULATIONS {player2.name} YOU WIN!!\
{LetCol.RESET}')
    print(f"Final Score:\n{player1.name}: {player1.score}\n\
{player2.name}: {player2.score}")

    player = createPlayer(1)
    computer = p("Computer")
    while(player.score < 100 and computer.score < 100):
        player = playerTurn(player)
        computer = computerTurn(computer, player)
        print(f'Your probabilities to win are: \
{prob.pWin(player.score, computer.score, 0):.2f}')

    if(player.score >= GOAL):
        print(f'{LetCol.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{LetCol.RESET}')
        print(f'{DIVIDER}')
    elif(computer.score >= GOAL):
        print(f'{LetCol.FAIL}You lose, computers > humans')
        print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")


def main():
    printWelcomeMessage()
    playersOPtion = showMenu()
    if playersOPtion == 1:
        playerVsMachine()
    else:
        playerVsPlayer()


if __name__ == '__main__':
    main()
