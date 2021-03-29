##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch5_HW
# Due Date: 03.29.21
# ####################################################



## Problem 17 - Prime Numbers

def main():
    print('\nIs Prime Number Program::\n')

    num = int(input('Enter a Real Number: '))
    
    result = is_Prime(num)

    if result: 
        print(f'{num} is Prime')
    else:
        print(f'{num} is NOT Prime')

def is_Prime(n) :
 
    # Base Cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
 
    # Skip middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
 
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True


## Solution 17
main()



## 18 - Prime Number List










## Problem 19 - Future Value

def main():
    P = float(input('Enter Acconut\'s Present Value: '))
    i = float(input('Enter Monthly Interest Rate (in percent):'))/100
    t = int(input('Enter # of Months: '))

    F =  futureValue(P, i, t)

    print(f'Future Value of the account ${F:,.2f} after a total of [{t}] Months\n')

def futureValue(pValue, mInterest, nMonths):
    fValue = pValue * (1 + mInterest) ** nMonths

    return fValue

## Solution 19
main()



## 21 - Rock, Paper, Scissor Game

import random, sys

print(":: Rock + Paper + Scissors ::\n")

# Initialize Win, Loss & Tie Variables.
win = 0
loss = 0
tie = 0

# Loop GamePlays.
while True:
    print(f"Win: {win} | Losses: {loss} | Ties: {tie}")
    print("""\nEnter Your Move:\n
            [R] - Rock 
            [P] - Paper 
            [S] - Scissors 
            [Q] - Quit Game\n""")
    userMove = input("\nType your Selection: ")
    userMove = userMove.lower()
    if userMove == 'q':
        sys.exit()   #Quit the program.

    # Display what the computer choice: 
    randomNumber = random.randint(1, 3)

    # Random CPU Selection 
    if randomNumber == 1:
        cpuMove = 'r'
        print("Rock")
    elif randomNumber == 2:
        cpuMove = 'p'
        print("Paper")
    elif randomNumber == 3:
        cpuMove = 's'
        print("Scissors")

    # Check Win
    if userMove == cpuMove:
        print("It is tie:!")
        tie += 1
    elif userMove == 'r' and cpuMove == 's':
        print("You win!")
        win += 1
    elif userMove == "p" and cpuMove == 'r':
        win += 1
        print("You win!")
    elif userMove == "s" and cpuMove == 'p':
        win += 1
        print("You win!")
    elif userMove == "r" and cpuMove == 'p':
        loss += 1
        print("You Lose!")
    elif userMove == "p" and cpuMove == 's':
        loss += 1
        print("You Lose!")
    elif userMove == "s" and cpuMove == 'r':
        loss += 1
        print("You Lose!")