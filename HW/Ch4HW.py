##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch4_HW
# Due Date: 03.07.21
# ####################################################

## 12 -- Calculating the Factorial of a Number

print()
num = int(input("Enter a Positive Integer: "))
print()


if num < 0:
    print('Factorial not defined for negative numbers. Try again!')
elif num == 0:
    print(f'The Factorial of {num} is 1')
else:
    factorial = 1
    for x in range(1, num+1):
        factorial = factorial * x
    print(f'{num}! is equal to {factorial}')
print()


## 13 -- Population

n_organisms = int(input('Starting number of organisms: '))
daily_p = float(input('Average daily increase (enter as a %): '))
n_days = int(input('Number of days to multiply: '))

## 15 -- Loop Pattern