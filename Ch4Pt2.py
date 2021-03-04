# ICA 2, Part 1

# total = 0
# howMany = int(input('How many numbers do you want? '))
# for x in range(1, howMany+1):
#     num = int(input(f'Enter number #{x}: '))
#     total += num
# print(f'The average is {total/howMany:.3f}')

# print()


# ICA 2, Part 2

total = 0
how_Many = 0
num = int(input('Enter a number: '))
while num != -1:
    total += num
    how_Many += 1
    num = int(input('Enter a number or -1 to quit: '))
print(f'The average is {total/how_Many:.3f}')