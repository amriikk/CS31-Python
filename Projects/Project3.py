##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Project 3
# Due Date: 06.03.21
# ####################################################

def main():
    d = {}
    infile = open('tv_shows.txt', 'r')
    ln = infile.readline()
    n = []
    while ln:
        title = ln.strip('\n').upper()
        num = infile.readline().strip('\n')
        n.append(num)
        star1 = infile.readline().strip('\n')
        star2 = infile.readline().strip('\n')
        star3 = infile.readline().strip('\n')
        star4 = infile.readline().strip('\n')
        ln = infile.readline()

        # Network Aired on
        if int(num[4]) == 1:
            cha = 'ABC'
        elif int(num[4]) == 2:
            cha = 'CBS'
        elif int(num[4]) == 3:
            cha = 'NBC'
        elif int(num[4]) == 4:
            cha = 'FOX'

        # Year Aired
        if int(num[0:2]) <= 18:
            first = 2000 + int(num[0:2])
        else:
            first = 1900 + int(num[0:2])

        for i in range(len(n)):
            a = n[i]
            s = a[2:4]
        
        # Last Year aired
        last = int(s) + first

        # Add elements to Dictionary
        d[title] = [star1, star2, star3, star4, first, last, cha]

    infile.close()

    # Print dictionary data
    for title in d:
        print(title, 'aired from', d[title][4], 'to', d[title][5], 'on', d[title][6])
        print('It starred ', d[title][0], ', ', d[title][1], ', ', d[title][2], ' and ', d[title][3], '.', sep='')

        print()

main()