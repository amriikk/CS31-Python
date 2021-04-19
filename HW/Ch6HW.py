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

## Problems 7 + 8 - Random Number File Writer | Reader

# # 7 and 8
# def main():
#     l = int(input("Enter the number of lines: "))
#     rand_numbers(l)
#     displayData()
#     golf()

# def rand_numbers(a):
#     outfile = open('randoms.txt', 'w')
#     for num in range(a):
#         y = str(random.randint(1, 500))
#         outfile.write(y + '\n')

# def displayData():
#     file = open('randoms.txt', 'r')
#     num = file.readline().rstrip('\n')
#     print(num)
#     while num != '':
#         num = file.readline().rstrip('\n')
#         print(num)
#     file.close()

# # outfile = open("random.txt", 'w')
# # rep = int(input("Enter amount of random numbers to generate: "))
# # for x in range(1,rep+1):
# #     number = random.randrange(501)
# #     outfile.write(number+"\n")
# # outfile.close()

# ## Problem 10 - Golf Scores


# # 6 & 9




# def golf():
#     outfile = open('golf.txt', 'w')
#     a = int(input('Enter the number of players: '))
#     for b in range(a):
#         name = input("Enter the player's name: ")
#         score = int(input("Enter the player's score: "))
#         outfile.write(name + "\t\t\t\t")
#         outfile.write(str(score) + "\n")
#     outfile.close()

#     infile1 = open('golf.txt', 'r')
#     line = infile1.readline().rstrip('\n')
#     print('player\t\t\tscore')
#     print(line)
#     while line != '':
#         line = infile1.readline().rstrip('\n')
#         print(line)

main()