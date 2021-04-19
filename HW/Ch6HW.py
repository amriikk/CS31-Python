##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch6_HW
# Due Date: 04.18.21
# ####################################################

## Problems 6 + 9 - Average of Numbers | Exception Handling
def displayData():
    infile = open('nba.txt','r')
    for name in infile:
        name = name.rstrip('\n')
        num = infile.readline().rstrip('\n')
        team = infile.readline().rstrip('\n')
        print(name,'wears number',num,'and plays for the',team)
    infile.close()

## Problems 7 + 8 - Random Number File Writer | Reader
outfile = open("random.txt", 'w')
rep = int(input("Enter amount of random numbers to generate: "))
for x in range(1,rep+1):
    number = random.randrange(501)
    outfile.write(number+"\n")
outfile.close()

## Problem 10 - Golf Scores