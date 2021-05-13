# Week 14, ICA 2
import pickle
def main():
    pacific = set()
    pacific.add('CA')
    pacific.add('NV')
    print('pacific =',pacific)
    mountain = set(['AZ', 'NM'])
    mountain.update(('UT','CO','WT','MT'))
    print('mountain =', mountain)
    combo = set(['OR','ID', 'ND', 'SD'])
    combo.remove('ND')
    combo.discard('SD')
    print('combo =',combo)
    temp = pacific | mountain # union
    west = temp | combo
    print('west =',west)
    pac = west & pacific # intersection
    mtn = west & mountain # intersection
    print('pac =',pac)
    print('mtn =',mtn)
    nocmb = west - combo # difference
    nopac = west - pacific 
    print('nocmb =', nocmb)
    print('nopac =', nopac)
    justone = west ^ combo
    nomtn = west ^ mountain
    print('justone =', justone)
    print('nomtn =', nomtn)
    # Part 2
    output = open('baseball.dat','bw')
    more = 'y'
    players1 = {}
    while more.lower() == 'y':
        players1['name'] = input('Enter name of baseball player: ')
        players1['team'] = input('Enter the player\'s team: ')
        players1['num'] = input('Enter the player\'s number: ')
        pickle.dump(players1,output)
        more = input('Got another one? (y/n) ')

    output.close()
    inFile = open('baseball.dat','br')
    eof = False
    players2 = {}
    while not eof:
        try: 
            players2 = pickle.load(inFile)
            print('Name: ',players2['name'])
            print('Team: ',players2['team'])
            print('Number: ',players2['num'])
            print()
        except EOFError:
            inFile.close()
            eof = True
main()
