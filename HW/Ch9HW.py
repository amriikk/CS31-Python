##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch7_HW
# Due Date: 05.14.21
# ####################################################

def main():
    # Problem 1 
    d1 = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    d2 = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    d3 = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m. ', 'CM241': '1:00 p.m.'}
    num = input('Enter Course #: ')
    num = num.upper()
    if num in d1:
        print('The room # for the Course', num, 'is', d1[num], 'with Professor', d2[num], '& meets at', d3[num])
    else:
        print('Course not Found.')
    print()

    # Problem 4
    infile = open('words1.txt', 'r')
    l = []
    for ln in infile:
        for ch in ln.split():
            l.append(ch)
    s = set(l)
    print(s)
    infile.close()
    print()

    # Problem 6
    # file 1
    infile1 = open('words1.txt', 'r')
    l1 = []
    for ln in infile1:
        for ch in ln.split():
            l1.append(ch)
    print('This are all the unique words in file 1:')
    s1 = set(l1)
    print(s1)
    print()
    # file 2
    infile2 = open('words2.txt', 'r')
    l2 = []
    for ln in infile2:
        for ch in ln.split():
            l2.append(ch)
    print('This are all the unique words in file 2:')
    s2 = set(l2)
    print(s2)
    print()
    print('This are the words that appear in both files:')
    b1 = s.intersection(l2)
    print(b1)
    print('\nThis are the words that appear in file 1 but not in file 2:')
    b2 = s1.difference(s2)
    if b2:
        print(b2)
    else:
        print('None')
    print('\nThis are the words that appear in file 2 but not in file 1:')
    b3 = s2.difference(s1)
    if b3:
        print(b3)
    else:
        print('None')
    print()
    print('This are the words that appear in either file 1 or file 2 but not in both:')
    b4 = s1.symmetric_difference(s2)
    if b4:
        print(b4)
    else:
        print('None')
    infile1.close()
    infile2.close()

main()