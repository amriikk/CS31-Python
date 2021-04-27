# Week 12, ICA 1

def main():
    marcel = get_goals('dionne.txt')
    total = get_total(marcel)
    print('Marcel Dionne scored', total, 'goals in', len(marcel), 'NHL seasons.')

def get_goals(filename):
    goals = [] # empty array
    file = open(filename, 'r')
    goals = file.readlines() # reads contents of file into list
    index = 0
    while index < len(goals):
        goals[index] = int(goals[index].rstrip('\n'))
        index += 1
    return goals

def get_total(a):
    total = 0
    for num in a:
        total += num
    return total



main()