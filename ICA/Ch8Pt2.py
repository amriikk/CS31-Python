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
    print('The data contains',low, 'lowercase letters,', up, 'uppercase letters,',digit, 'digits and', space, 'whitespace characters.')
    infile.close()
    # Part 2
    infile = open('OneWordMovieTitles.txt','r')
    movies = infile.read()
    print(movies.upper())
    print(movies.lower())
    if movies.startswith('Deliv'):
        print('Deliverance comes first in the movies string')
    else:
        print('Deliverance does not come first in the movies string')
    if movies.endswith('site'):
        print('Parasite comes last in the movies string')
    else:
        print('Parasite does not come last in the movies string')
    jaws = movies.find('Jaws')
    if jaws != -1:
        print('Jaws is at the index', jaws, 'in the movies string' )
    else:
        print('Jaws is not in the movies string ')
    movies = movies.replace('Babe', 'Aladdin')
    print(movies)
    infile.close()
    # Part 3
    fullname = input('Enter your first, middle and last name, seperated by spaces: ')
    name = fullname.split()
    print('Here are your initials: ', name[0][0].upper(), '. ', name[1][0].upper(), '. ', name[2][0].upper())

main()