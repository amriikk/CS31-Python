# Week 11 - ICA 1
import random

def main():
    pickfour = [0]*4
    # print(pickfour)
    x = 0
    while x < 4:
        pickfour[x] = random.randint(0,9)
        x += 1
    # end while loop
    print('\nPickfour elements in order')
    for x in pickfour:
        print(x, end=' ')
    print()
    print('\nPickfour elements in reverse order')
    for x in range(-1, -5, -1):
        print(pickfour[x], end=' ')
    print()

    # Part 2
    OrigSixTeams = ["Canadiens", "Maple Leafs", "Bruins", "Black Hawks", "Red Wings", "Rangers"]
    OrigSixYears = [1917,1917,1924,1926,1926,1926]
    NextSixtTeams = ['Kings', 'North Stars', 'Seels', 'Flyers', 'Penguins', 'Blues']
    print('Original Six NHL teams based in Canada: ', OrigSixTeams[:2])
    print('Original Six NHL teams based in USA: ', OrigSixTeams[2:])

main()