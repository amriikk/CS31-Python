# Week 13, ICA 1

def main():
    sum = 0
    again = 'y'
    while again == 'y' or again == 'Y':
        nums = input('Enter a sequence of numbers: ')
        for ch in nums:
            sum += int(ch)
        print('Sum of digits in', nums, '=', sum)
        sum = 0
        again = input('Care to try again? (y/n) ')

main()