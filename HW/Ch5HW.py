##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch5_HW
# Due Date: 03.29.21
# ####################################################



# ## Problem 17 - Prime Numbers

# def main():
#     print('\nIs Prime Number Program::\n')

#     num = int(input('Enter a Real Number: '))
    
#     result = is_Prime(num)

#     if result: 
#         print(f'{num} is Prime\n')
#     else:
#         print(f'{num} is NOT Prime\n')

# def is_Prime(n) :
 
#     # Base Cases
#     if (n <= 1) :
#         return False
#     if (n <= 3) :
#         return True
 
#     # Skip middle five numbers in below loop
#     if (n % 2 == 0 or n % 3 == 0) :
#         return False
 
#     i = 5
#     while(i * i <= n) :
#         if (n % i == 0 or n % (i + 2) == 0) :
#             return False
#         i = i + 6
 
#     return True


# ## Solution 17
# main()



# ## 18 - Prime Number List










## Problem 19 - Future Value

def futureValue():
    P = float(input('Enter Acconut\'s Present Value: '))
    i = float(input('Enter Monthly Interest Rate (in percent):'))/100
    t = int(input('Enter # of Months: '))

    F =  futureV(P, i, t)

    print(f'Future Value of the account ${F:,.2f} after a total of [{t}] Months\n')

def futureV(pValue, mInterest, nMonths):
    fValue = pValue * (1 + mInterest) ** nMonths

    return fValue

## Solution 19
futureValue()


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
            [1] - Rock 
            [2] - Paper 
            [3] - Scissors 
            [4] - Quit Game\n""")
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
                [1] Yes 
                [2] No\n''').lower()

    if re == 'y':
        print('Ready, Set, PLAY!\n')
        gamePlay()
    elif re == 'n':
        print('Thanks for playing!\n')
        sys.exit()
    else:
        print('Invalid!')
        sys.exit()

## Solution 21
gamePlay()

