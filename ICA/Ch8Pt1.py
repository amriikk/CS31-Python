# Week 13, ICA 1

def main():
    # Part 1
    sum = 0
    again = 'y'
    while again == 'y' or again == 'Y':
        nums = input('Enter sequence of numbers: ')
        for ch in nums:
            sum += int(ch)
        print('Sum of digits in', nums, '=', sum)
        sum = 0
        again = input('Care to try again? (y/n) ')
    # Part 1
    print()
    again = 'y'
    while again == 'y' or again == 'Y':
        title = input('Enter the movie title: ')
        if len(title) <= 4:
            codept1 = title
        elif len(title) == 5:
            codept1 = title[:len(title):2]
        else: 
            codept1 = title[:5:2] + title[-1]
        year = input('Enter the 4-digit year movie was released: ')
        codept2 = year[2:]
        print('Code for', title, 'is', codept1 + codept2)
        again = input('Try again? (y/n) ')
        
main()