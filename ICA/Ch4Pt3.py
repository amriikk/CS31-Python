# ICA 3, Part 1

# players = int(input('Enter number of players: '))
# seasons = int(input('Enter number of seasons: '))

# for x in range(players):
#     total = 0
#     name = input('Enter the name of a hockey player ')
#     for y in range(1, seasons+1):
#         goals = int(input(f'Enter goals scored in season #{y}: '))
#         total += goals 
#     print(name, 'has scored', total, "goals in the last", seasons, "seasons.")

# ICA 3, Part 2

BASE_SIZE = 8
for row in range(BASE_SIZE, 0, -1):
    for col in range(row+1):
        print('*', end='')
    print()
print()

NUM_STEPS = 6
for row in range(NUM_STEPS, 0, -1):
    for col in range(row-1):
        print(' ', end='')
    print('#')
print()

# ICA 3, Part 3

for x in range(7):
    for y in range(x):
        print('$', end='')
    for z in range(6-x):
        print('#', end='')
    print()