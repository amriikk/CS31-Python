# Week 11, ICA 2

def main():
    # Parts 1 + 2
    numbers = [] # creates an empty list
    more = 'y'
    while more == 'y':
        num = int(input('Enter a retired Angel\' number: '))
        numbers.append(num) # adds num to end of numbers list
        more = input('Got another one? (y/n)')
    print(numbers)
    numbers.remove(33)
    numbers.insert(4,40)
    print('After remove and insert:', numbers)
    try:
        here = numbers.index(40)
        print('Found 40 at index', here)
    except ValueError:
        print('40 is the not in the list')
    del numbers[numbers.index(40)]
    print('After del: ', numbers)
    numbers.reverse()
    print('After reverse:',numbers)
    numbers.sort()
    print('After sort:', numbers)
    print('Max:', max(numbers))
    print('Min:', min(numbers))
    # Part 3
    numbers2 = numbers + [44,22,55]
    total, average = get_total_average(numbers2)
    print(f'Total = {total}, Average = {average:.2f}')

def get_total_average(theList):
    total = 0.0
    for num in theList:
        total += num
    average = total / len(theList)
    return total, average

main()