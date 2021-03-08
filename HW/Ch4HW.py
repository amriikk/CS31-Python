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

print()
n_organisms = int(input('Starting number of organisms: '))
daily_p = float(input('Average daily increase (enter as a [%]): '))/100
n_days = int(input('Number of days to multiply: '))

day1 = True
print("\nDay Approximate\tPopulation")
print('-----------------------------')
for x in range(n_organisms, n_days+1):
    if day1:
        print(1, '\t\t', n_organisms)
        day1 = False
    add = n_organisms * daily_p
    n_organisms = n_organisms + add
    print(f'{x}', '\t\t', '{0:.6f}'.format(n_organisms))
print()

## 15 -- Loop Pattern

print()
for row in range(6):
    print('#', end='', sep='')
    for space in range(row):
        print(' ', end='', sep='')
    print('#', sep='')