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
    return option



def main():
    printWelcomeMessage()
    playersOPtion = showMenu()
    if playersOPtion == 1:
        print(12)
    else:
        print(45)
    

if __name__ == '__main__':
    main()