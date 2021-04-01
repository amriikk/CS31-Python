## Midterm Part 2

# Question 1:

# x = 10.0
# y = 5
# z = 8 

# print((x + 4) / (y + 2))
# print((y + 5) // (z - 2)) 
# print((y + 3) * (x - 2))  
# print((z + 9) - (y - 3)) 
# print((y - 3) ** (z - 5))

# Question 2:

# x = 'Muldoon'
# y = 'Mulroney'
# z = 'Mulcahey'
# w = 'Muldrow'

# print(x >= y)
# print(y < z or x > w)
# print(x < z and y < x) 
# print(not(z > w)) 
# print(not(z >= y) and not(x != w))

# Question 3:

# print(format(33333.98765,'8,.1f')) 
# print(format(33333.98765,'9.3f'))
# print(format(33333.98765,'11,.4f'))
# print(format(33333.98765,'9.3f')) 
# print(format(33333.98765,'6.1f'))

# Question 4:

def main():
    ch = str(input('Enter G, H, P or S: '))#.upper() #Uppercase input
    print(arena(ch))

def arena(cha):
    if cha == 'G' or cha == 'g' :
        stadium = 'The Gaylord Center is home to the USC Trojans'
    elif cha == 'H' or cha == 'h':
        stadium = 'The Honda Center is home to the Anaheim Ducks'
    elif cha == 'P' or cha == 'p':
        stadium = 'Pauley Pavilion is home to the UCLA Bruins'
    elif cha == 'S' or cha == 's':
        stadium = 'The Staples Center is home to the LA Lakers, Kings, and Clippers'
    else:
        stadium = 'Invalid character entered'
    return stadium

# Solution 4:
main()


# # Question 5:

# def main():
#     num1 = float(input('Input first number: '))
#     num2 = float(input('Input second number: '))
#     getsum(num1, num2)

# def getsum(x, y):
#     if x > 10 and y < 5:
#         sum = (3 * x) + (2 * y)
#         print(f'The sum of {x} + {y} is equal to {sum:.3f}')
#     elif x >= 15 and y > 7:
#         sum = (x / 3) + (y ** 2)
#         print(f'The sum of {x} + {y} is equal to {sum:.2f}')
#     elif x < 4 and y >= 10:
#         sum = (x ** 3) + (y / 5)
#         print(f'The sum of {x} + {y} is equal to {sum:.4f}')
#     else: 
#         sum = x + y
#         print(f'The sum of {x} + {y} is equal to {sum:.1f}')

# #Solution 5:
# main()

# Question 6:

import random

def main():
    howmany = int(input('How many numbers? '))
    big, small = bigsmall(howmany)
    print('Of the numbers generated,', big, 'were greater than 50', small, 'were 50 or less.')

def bigsmall(num):
    big = 0
    small = 0

    if num <= 1:
        print('Must be greater than 1. Try again')
        howmany = int(input('How many numbers? '))
        big, small = bigsmall(howmany)

    while num > 1:
        for x in range(num):
            y = random.randint(1,200)
            print(f'Number {x+1} = {y}')
            if y > 50:
                big = big + 1
            else: 
                small = small + 1
            num = num - 1

    return big, small

# Solution 6:
main()