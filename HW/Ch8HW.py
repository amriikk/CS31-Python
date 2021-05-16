##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch7_HW
# Due Date: 05.07.21
# ####################################################

## Problem 3
def main():
    date = input('Enter date to be converted (Format: mm/dd/yyyy): ')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    d = date.split('/')
    month = int(d[0])
    for n in range(12):
        m = months[month-1]
    day = int(d[1])
    year = int(d[2])
    print(m + ' ', day, ', ', year, sep='')
    print()

 ## Problem 4
    a = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....','..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']
    print('--Morse code conversion--')
    mc = input('Enter a string: ')
    t = mc.upper()
    t.split()
    x = []
    for i in range(len(t)):
        w = t[i]
        x.append(b[a.index(w)])
    index = 0
    for j in x:
        print(x[index], end=' ')
        index += 1
    print()

 ## Problem 5
    print()
    t = input('Enter a phone number (Format: xxx-xxx-xxxx): ')
    t.split('-')
    ph = []
    phone = ""
    two = ['A', 'B', 'C']
    three = ['D', 'E', 'F']
    four = ['G', 'H', 'I']
    five = ['J', 'K', 'L']
    six = ['M', 'N', 'O']
    seven = ['P', 'Q', 'R', 'S']
    eight = ['T', 'U', 'V']
    nine = ['W', 'X', 'Y', 'Z']
    for num in t[1:2]:
      for l in t:
        if l.isdigit():
          ph.append(l)
        elif l.upper() in two:
          ph.append('2')
        elif l.upper() in three:
          ph.append('3')
        elif l.upper() in four: 
          ph.append('4')
        elif l.upper() in five:
          ph.append('5')
        elif l.upper() in six:
          ph.append('6')
        elif l.upper() in seven:
          ph.append('7')
        elif l.upper() in eight:
          ph.append('8')
        elif l.upper() in nine:
          ph.append('9')
    pt1 = ph[0:3]
    pt2 = ph[3:6]
    pt3 = ph[6:10]
    print('(', *pt1, ')', *pt2, '-', *pt3, sep=' ')

main() ## call main