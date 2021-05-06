# Week 13, ICA 2

def main():
    infile = open('text.txt', 'r')
    data = infile.read()
    low = 0
    up = 0
    digit = 0
    space = 0
    for ch in data:
        if ch.islower():
            low += 1
        elif ch.isupper():
            up += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            space += 1
    print('The data contains',low, 'lowercase letters,', up 'uppercase letters,',digit, 'digits and', space, 'whitespace characters.')
    infile.close()


main()