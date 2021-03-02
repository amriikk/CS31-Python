# ICA 1

more = 'y'
while more == 'y' or more == 'Y':
    number = int(input('Enter a number: '))
    if number > 25:
        print(number, 'is greater than 25.')
    else: 
        print(number,'is 25 or less.')
    more = input('Wanna do this again? (y/n): ')

# Part 2

howHigh = int(input('How big a number you want? '))
print("\nNumber\tCubes")
print('--------------')
for x in range(1, howHigh+1):
    print(x, '\t', x**3)

print()

start = int(input('Where do you want to start? '))
end = int(input('Where do you want to end? '))
step = int(input('Step value? '))
print("\nNumber\tCubes")
print('--------------')
for x in range(start,end+1,step):
    print(f'{x:<3,d}', '\t', x**3)
print()

# Part 4

for x in range(8, -3, -1):
    print(x, end=' ')
print()

for x in range(30, 1, -7):
    print(x, end=' ')
print()