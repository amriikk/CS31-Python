# ## Problem 19 - Future Value

# def main():
#     P = float(input('Enter Acconut\'s Present Value: '))
#     i = float(input('Enter Monthly Interest Rate (in percent):'))/100
#     t = int(input('Enter # of Months: '))

#     F =  futureValue(P, i, t)

#     print(f'Future Value of the account ${F:,.2f} after a total of [{t}] Months')

# def futureValue(pValue, mInterest, nMonths):
#     fValue = pValue * (1 + mInterest) ** nMonths

#     return fValue

# ## Solution 19
# main()

# ## 21 - Rock, Paper, Scissor Game

# import random, sys

# print("\n:: Rock + Paper + Scissors ::\n")

# # Initialize Win, Loss & Tie Variables.
# win = 0
# loss = 0
# tie = 0

# # Loop GamePlays.
# while True:
#     print(f'Win: {win} | Losses: {loss} | Ties: {tie}')
#     print("""\nEnter Your Move:\n
#             [1] - Rock 
#             [2] - Paper 
#             [3] - Scissors 
#             [4] - Quit Game\n""")
#     uSelection = int(input('\nType your Selection: '))
    
#     if uSelection == 4:
#         print('Thanks for playing')
#         sys.exit()   # Quit the Game Loop - exit()
#     else:
#         print('Invalid move! CPU Wins')
#         sys.exit()

#     # User Selection
#     if uSelection == 1:
#         userMove = 'r'
#         print("Your Selection: Rock")
#     elif uSelection == 2:
#         userMove = 'p'
#         print("Your Selection: Paper")
#     elif uSelection == 3:
#         userMove = 's'
#         print("Your Selection: Scissors")

#     # Random CPU Selection 
#     randomNumber = random.randint(1, 3)

#     # Display what the computer choice: 
#     if randomNumber == 1:
#         cpuMove = 'r'
#         print("CPU Selection: Rock")
#     elif randomNumber == 2:
#         cpuMove = 'p'
#         print("CPU Selection: Paper")
#     elif randomNumber == 3:
#         cpuMove = 's'
#         print("CPU Selection: Scissors")

#     # Check Win
#     if userMove == cpuMove:
#         print("It is tie:!")
#         tie += 1
#     elif userMove == 'r' and cpuMove == 's':
#         print("You win!")
#         win += 1
#     elif userMove == "p" and cpuMove == 'r':
#         win += 1
#         print("You win!")
#     elif userMove == "s" and cpuMove == 'p':
#         win += 1
#         print("You win!")
#     elif userMove == "r" and cpuMove == 'p':
#         loss += 1
#         print("You Lose!")
#     elif userMove == "p" and cpuMove == 's':
#         loss += 1
#         print("You Lose!")
#     elif userMove == "s" and cpuMove == 'r':
#         loss += 1
#         print("You Lose!")

list1 = [1, 2, 3]
list2 = []
for element in list1:
list2.append(element)
list1 = [4, 5, 6]