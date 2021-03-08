##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch4_HW
# Due Date: 03.07.21
# ####################################################

## 12 -- Calculating the Factorial of a Number

num = int(input("Enter a Positive Integer: "))
print()
factorial = 1

if num < 0:
    print('Factorial not defined for negative numbers. Try again!')
elif num == 0:
    print(f'The Factorial of {num} is 1')
else:
    for x in range(1, num+1):
        factorial *= num
        print(f'The factorial of {num:.3f} is {factorial}')
print()


## 13 -- Population


## 15 -- Loop Pattern