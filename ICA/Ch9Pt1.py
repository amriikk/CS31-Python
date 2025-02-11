def main():
    # Part 1
    schools1 = {'USC':'Lost Angeles','Oregon':'Eugene',
                'Arizona':'Tempe','Utah':'Salt Lake City'}

    schools2 = {'USC':'Trojans','Oregon':'Ducks','Arizona':'Wildcats',
                'Utah':'Utes'}
    again = 'y'
    while again.lower() == 'y':
        school = input("Enter the name of school: ")
        if school in schools1:
            print(school, 'Location:',schools1[school],'Nickname:',schools2[school])
        else:
            print("That school is invalid.")

        again = input("Wanna do this again? (y/n) ")
    # Part 2
    medals = {'Norway':[14,14,11],'Germany':[14,10,7],'Canada':[11,8,10]}
    medals['USA'] = [9,8,6]
    medals['Netherlands'] = [8,6,6]
    medals['Sweden'] = [7,6,1]
    print('Medal Count for 2018 Winter Olympics')
    displayData(medals)
    countries = medals.keys()
    for c in countries:
        print(c, '  ',end='')
    print()
    lists = medals.values()
    print(lists)
    for x in lists:
        print(x)
    sweden = medals.pop("Sweden","Not in the list")
    print("Sweden data:",sweden)
    print("New Medal Count for 2018 Winter Olympics")
    displayData(medals)

def displayData(d):
    for key in d:
        print(key,'won',d[key][0],'gold medals,',d[key][1],'silver medals, and',
              d[key][2],'bronze medals')
              
main()