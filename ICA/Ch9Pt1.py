# Week 14, ICA 1 

def main():
  # Part 1 
  schools1 = {'USC':'Los Angeles', 'Oregon': 'Eugene', 'Arizona':'Tempe', 'Utah' :'Salt Lake City'}
  schools2 = {'USC':'Trojans','Oregon':'Ducks','Arizona':'Wildcat','Uath':'Utes'}
  again ='y'
  while again == 'y' or again == 'Y':
    school = input('Enter name of school: ')
    if school in schools1: 
        print(school,'Location:',schools1[school],'Nickname:',schools2[school])
    else:
        print('That school is invalid')
    again = input('Wanna do this again? (y/n) ')
  # Part 2 
  print()
  medals = {'Norway':[14,14,11],'Germany':[14,10,7], 'Canda':[11,8,10]}
  medals['USA'] = [9,8,6]
  medals['Netherlands'] = [8,6,6]
  medals['Swedan'] = [7,6,1]
  print('Medals Count for 2018 Winter Olympics')
  displayData(medals)
  countries = medals.key()
  for c in countries:
    print(c, '  ',end='')
  print()
  lists = medals.values()
  print(lists)
  for x in lists:
    print(x)
  swedan = medals.pop('Swedan', 'No aqui')
  print('Swedan data:',swedan)
  print('New Medals Count for 2018 Winter Olympics')
  displayData(medals)

def displayData(d):
  for key in d:
    print(key, 'won',d[key][0],'gold medals',d[key][1],'silver medals, and',d[key][2],
    'bronze medals')

main()