# ICA 1 -- Teams
def main():
    team = int(input('Type 1 for Kings, 2 for Ducks, 3 for Knights, 4 for Coyotes or anything else to quit: '))
    while team >= 1 and team <= 4:
        if team == 1:
            kings()
        elif team == 2:
            ducks()
        elif team == 3:
            knights()
        else:
            yotes()
        input('Press Enter to continue.. ')
        team = int(input('Type 1 for Kings, 2 for Ducks, 3 for Knights, 4 for Coyotes or anything else to quit: '))
    print('That\'s all!')

def kings():
    print('Los Angeles Kings - began NHL play in 1967')
    print('Home arena is Staple Center')
    print()

def ducks():
    print('Anaheim Ducks - began NHL play in 1993')
    print('Home arena is Honda Center')
    print()

def knights():
    print('Vegas Golden Knights - began NHL play in 2017')
    print('Home arena is T-Mobile Center')
    print()

def yotes():
    print('Arizona Coyotes - began NHL play in 1979 as Winnipeg Jets')
    print('Moved to Arizona in 1996')
    print('Home arena is Gila River Center')
    print()

# Call main()
print()
main()