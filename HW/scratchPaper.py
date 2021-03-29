## 21 - Rock, Paper, Scissor Game

import random, sys

print("\n:: Rock + Paper + Scissors ::\n")

# Initialize Win, Loss & Tie Variables.
win = 0
loss = 0
tie = 0

# Loop GamePlays.
while True:
    print(f'Win: {win} | Losses: {loss} | Ties: {tie}')
    print("""\nEnter Your Move:\n
        [1] - Rock 
        [2] - Paper 
        [3] - Scissors 
        [4] - Quit Game\n""")
    uSelection = int(input('\nType your Selection: '))
    
    # User Selection
    if uSelection == 1:
        userMove = 'r'
        print("Your Selection: Rock")
    elif uSelection == 2:
        userMove = 'p'
        print("Your Selection: Paper")
    elif uSelection == 3:
        userMove = 's'
        print("Your Selection: Scissors")
    elif uSelection == 4:
        print('Thanks for playing!!')
        sys.exit()   # Quit the Game Loop - exit()
    else:
        print('\tInvalid Selection! Please try again..\n')
        uSelection = int(input('\nType your Selection: '))


    # Random CPU Selection 
    randomizeNum = random.randint(1, 3)

    # Display CPU Selection: 
    if randomizeNum == 1:
        cpuMove = 'r'
        print("CPU Selection: Rock")
    elif randomizeNum == 2:
        cpuMove = 'p'
        print("CPU Selection: Paper")
    elif randomizeNum == 3:
        cpuMove = 's'
        print("CPU Selection: Scissors")

    # Check Win + Game Counters
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