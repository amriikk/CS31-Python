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
    print('Pickfour elements in order')
    for x in pickfour:
        print(x, end=' ')
    print()
    print('Pickfour elements in reverse order')
    for x in range(-1, -5, -1):
        print(pickfour[x], end=' ')
    print()


main()