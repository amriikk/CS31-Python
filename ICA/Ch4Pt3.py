# ICA 3, Part 1

players = int(input('Enter number of players: '))
seasons = int(input('Enter number of seasons: '))

for x in range(players):
    total = 0
    name = input('Enter the name of a hockey player ')
    for y in range(1, seasons+1):
        goals = int(input(f'Enter goals scored in season #{y}: '))
        total += goals 
    print(name, 'has scored', total, "goals in the last", seasons, "seasons.")

#