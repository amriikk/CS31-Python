##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch6_HW
# Due Date: 04.18.21
# ####################################################

def main():
    getAverage()

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
# outfile = open("random.txt", 'w')
# rep = int(input("Enter amount of random numbers to generate: "))
# for x in range(1,rep+1):
#     number = random.randrange(501)
#     outfile.write(number+"\n")
# outfile.close()

## Problem 10 - Golf Scores

main()