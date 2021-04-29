# Week 12, ICA 2

def main():
    premier = ('Liverpool','Chelsea','Arsenal','Southampton')
    mls = ('LAFC','LA Galaxy','DC United','Sporting KC')
    for epl in premier:
        print(epl)
    print()
    for x in range(4):
        print(mls[x])
    #unpack MLS tuple
    mls1, mls2, mls3, mls4 = mls
    print()
    print(mls1,'and',mls2,'and',mls3,'and',mls4)
    soccer_teams = list(premier)
    soccer_teams.append(mls1)
    soccer_teams.append(mls2)
    soccer_teams.append(mls3)
    soccer_teams.append(mls4)
    print(soccer_teams)
    soccer_teams2 = tuple(soccer_teams)
    print(soccer_teams2)

main()