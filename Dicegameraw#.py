from random import randint

GOAL = 100

def printWelcomeMessage():
    print('Welcome to the dice game PIG')
    print('In this game wins the first player to reach 100 points')
    print(' Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1.')

def showMenu():
    print('Press 1 to play vs the computer')
    print('Press 2 for 2 players')
    choice = [1,2]
    option = 0
    while(option not in choice):
        try:
            option = int(input('Please input 1 or 2 depending on your choice: '))
        except ValueError:
            print('Please enter a valid value (1, 2)')
            print('\n')
    return option

def showOptionMenu():
    print('Enter 1 to roll the dice')
    print('Enter 2 to hold your score')
    option2 = int(input('Enter your choice: '))
    return option2



def playerVsMachine():
    player1Score = 0
    computerScore = 0
    keepRunning = True
    while(keepRunning):
        player1Score = playerTurn(player1Score)
        if(player1Score >= GOAL):
            print('CONGRATULATIONS YOU WIN!! Humans > Computers')
            keepRunning = False
        computerScore = computerTurn(computerScore,player1Score)
        if(computerScore >= GOAL):
            print('You lose, computers > humans')
            keepRunning = False
    print(f"Final Score:\n Player: {player1Score} \n Computer: {computerScore}")

def  playerTurn(score):
    option = 0
    turnScore = 0
    keepRunning = True
    while(keepRunning):
        option = showOptionMenu()
        if (option ==2):
            keepRunning = False
        else:
            x = roll()
            
            if(x==1):
                print("Unlucky, you scored a 1")
                print(f"Your score this turn is {score}")
                print('\n')
                return score
            else:
                print(f"You got a {x}")
                turnScore += x
                print(f'Your total score for this turn is: {turnScore}')
                print('\n')
    score += turnScore
    print(f"Your score this turn is {score}")
    print('\n')

    return score

def  computerTurn(i,j):
    dice = 0
    k = 0
    keepRolling = True
    while(k < 20):
        dice = roll()
        if(dice==1):
            print(f"Computer score this turn is {i}")
            print('\n')
            return i
        else:
            k += dice
    i += k
    print(f"Computer score this turn is {i}")
    print('\n')
    return i



def roll():
    score = randint(1,6)
    return score 


def main():
    printWelcomeMessage()
    playersOPtion = showMenu()
    if playersOPtion == 1:
        playerVsMachine()
    else:
        print(45)
    

if __name__ == '__main__':
    main()