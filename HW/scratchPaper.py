## 21 - Rock, Paper, Scissor Game

import random, sys

print("\n:: Rock + Paper + Scissors ::\n")

def gamePlay():
    play = True

    # Initialize Win, Loss & Tie Variables.
    win = 0
    loss = 0
    tie = 0

    while play:

        print(f'\nWin: {win} | Losses: {loss} | Ties: {tie}')
        print("""\nEnter Your Move:\n
            1 - Rock 
            2 - Paper 
            3 - Scissors 
            4 - Quit Game\n""")
        uSelection = int(input('\nType your Selection: '))

        userMove = userSelection(uSelection)
        cpuMove = randomCPU()
        tallyCount = checkWins(userMove, cpuMove)

        if tallyCount == 1:
            tie = tie + 1
        elif tallyCount == 2:
            win = win + 1
        elif tallyCount == 3:
            loss = loss + 1

    ## Ask user to play again!
    rePlay()
    

# User Selection method
def userSelection(uSelection):    
    if uSelection == 1:
        userMove = 'r'
        print("Your Selection:\tRock")
        return userMove
    elif uSelection == 2:
        userMove = 'p'
        print("Your Selection:\tPaper")
        return userMove
    elif uSelection == 3:
        userMove = 's'
        print("Your Selection:\tScissors")
        return userMove
    elif uSelection == 4:
        print('\nThanks for playing!!\n')
        # Quit the Game Loop - exit()
        sys.exit()
    else:
        print('\tInvalid Selection! CPU Wins\n')
        rePlay()
    

# Random CPU Selection
def randomCPU():
    randomizeNum = random.randint(1, 3)

    # Display CPU Selection: 
    if randomizeNum == 1:
        cpuMove = 'r'
        print("CPU Selection:\tRock")
        return cpuMove
    elif randomizeNum == 2:
        cpuMove = 'p'
        print("CPU Selection:\tPaper")
        return cpuMove
    elif randomizeNum == 3:
        cpuMove = 's'
        print("CPU Selection:\tScissors")
        return cpuMove

# Check Win + Game Counters
def checkWins(userMove, cpuMove):
    if userMove == cpuMove:
        print("It is tie:!")
        tie = 1
        return tie
    elif userMove == 'r' and cpuMove == 's':
        print("You Win!")
        win = 2
        return win
    elif userMove == "p" and cpuMove == 'r':
        win = 2
        print("You Win!")
        return win
    elif userMove == "s" and cpuMove == 'p':
        win = 2
        print("You Win!")
        return win
    elif userMove == "r" and cpuMove == 'p':
        loss = 3
        print("You Lose!")
        return loss
    elif userMove == "p" and cpuMove == 's':
        loss = 3
        print("You Lose!")
        return loss
    elif userMove == "s" and cpuMove == 'r':
        loss = 3
        print("You Lose!")
        return loss

def rePlay():
    re = input('''Play Again? 
                [Y] Continue.. 
                [N] Game Over!\n''').lower()

    if re == 'y':
        print('Ready, Set, PLAY!\n')
        gamePlay()
    elif re == 'n':
        print('\tGame Over!\n')
        sys.exit()
    else:
        print('\tInvalid!')
        sys.exit()

## Solution 21
gamePlay()


def rePlay():
    re = int(input('''Play Again? 
                [1] Yes 
                [2] No\n'''))

    if re == 1:
        print('Ready, Set, PLAY!\n')
        gamePlay()
    elif re == 2:
        print('Thanks for playing!\n')
        sys.exit()
    else:
        print('Invalid!')
        sys.exit()

