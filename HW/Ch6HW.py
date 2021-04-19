##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch6_HW
# Due Date: 04.18.21
# ####################################################
import os
import random

def main():
    try:
        getAverage()
    except IOError:
        print('File did not open')
    except ValueError as zuh:
        print(zuh)
    finally:
        print('Moving on..')

## Problems 6 + 9 - Average of Numbers | Exception Handling
def getAverage():
    sum = 0
    count = 0
    infile = open('numbers.txt','r')
    for num in infile:
        num = num.rstrip('\n')
        sum += int(num)
        print(num,'is added. New total:', sum)
        count += 1
    avg = sum / count
    print('Average of the numbers in the file: ', avg)
    infile.close()

# Problems 7 + 8 - Random Number File Writer | Reader

def main():
    uIn = int(input("Enter amount of random numbers to generate: "))
    randNum(uIn)
    displayData()
    golf()

def randNum(a):
    outfile = open('randoms.txt', 'w')
    for num in range(a):
        x = str(random.randint(1, 500))
        outfile.write(x + '\n')

def displayData():
    file = open('randoms.txt', 'r')
    num = file.readline().rstrip('\n')
    print(num)
    while num != '':
        num = file.readline().rstrip('\n')
        print(num)
    file.close()

# Problem 10 - Golf Scores

def golf():
    outfile = open('golf.txt', 'w')
    n = int(input('Enter number of players: '))
    for i in range(n):
        name = input("Enter player's name: ")
        score = int(input("Enter player's score: "))
        outfile.write(name + "\t\t\t")
        outfile.write(str(score) + "\n")
    outfile.close()

    infile1 = open('golf.txt', 'r')
    l = infile1.readline().rstrip('\n')
    print('\nPlayer\t\t\tScore')
    print(l)
    while l != '':
        l = infile1.readline().rstrip('\n')
        print(l)

main()