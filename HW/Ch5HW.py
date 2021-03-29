##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch5_HW
# Due Date: 03.29.21
# ####################################################

## Problem 17 - Prime Numbers

def main():
    print('Is Prime Number Program::\n')

    num = int(input('Enter a Real Number: '))
    
    result = is_Prime(num)

    if result: 
        print(f'{num} is Prime')
    else:
        print(f'{num} is NOT Prime')

def is_Prime(n) :
 
    # Base Cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
 
    # This is checked so that we can skip
    # Skip middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
 
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True


## Solution 18 - Prime Number List
main()



# num = int(input('Enter a number: '))

# if (isPrime(num)) :
#     print(f"Is  True")
# else :
#     print(f"Is False")


## 18 














## 21 - Rock, Paper, Scissor Game