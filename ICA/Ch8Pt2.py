# Week 13, ICA 2
def main():
    # Part 1
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
    print('The data contains', low, 'lowercase letters,', up, 'uppercase letters,', digit, 'digits', space,
          'whitespace Characters.')
    infile.close()
    print()
    # Part 2
    infile = open('OneWordMovieTitles.txt', 'r')
    movies = infile.read()
    print(movies.upper())
    print(movies.lower())
    if movies.startswith('Deliv'):
        print('Deliverance comes first in the movies string')
    else:
        print('Deliverance does not come first in the movies string')
    if movies.endswith('site'):
        print('Parasite does not come first in the movies string')
    jaws = movies.find('Jaws')
    if jaws != -1:
        print('Jaws is at index', jaws, 'in the movies string')
    else:
        print('Jaws is not in the movies string')
    movies = movies.replace('Babe', 'Aladdin')
    print(movies)
    infile.close()
    print()
    # Part 3
    fullname = input('Enter your first, middle, and last name, separated by blanks spaces: ')
    name = fullname.split()
    print('Here are your initials: ', name[0][0].upper(), '.', name[1][0].upper(), '.', name[2][0].upper(), '.', sep='')

# Don't forget to call main
main()
