# CS31: Introduction to Python

## Question 1
print()
matrix = [[0,0,0,0,0],[0,0,0,0,0]]
inFile = open('nums.txt', 'r')
for x in range(2):
    for y in range(5):
        num = int(inFile.readline())
        if num < 10:
            matrix[x][y] = 2 * (num - 3)
        else:
            matrix[x][y] = 5 + num // 4
print(matrix)

## Question 2
print()
list1 = [5,6,7,8,9,10,11,12,13,14]
print('#1:', list1[:4])
print('#2:', list1[-3:])
print('#3:', list1[-5:-2])
print('#4:', list1[3:6])
print('#5:', list1[2:7:3])


## Question 3
print()
list2 = ['q','r','s','t','u','v','w','x','y','z']
print('#1:', list2[2:4])
print('#2:', list2[-7:-4])
print('#3:', list2[-8:-4])
print('#4:', list2[1:9:3])
print('#5:', list2[-8:-1:4])

## Question 4
print()
set1 = set([11,22,33,44,55,66,77])
set2 = set([22,33,44,55])
print('#1:', set1 | set2)
print('#2:', set1 & set2)
print('#3:', set1 - set2)
print('#4:', set1 ^ set2)
print('#5:', set2 <= set1) # true

## Question 5
print()
set1 = set([1,2,3,4,5,6,7])
set2 = set([3,4,5,6,7,8])
print('#1:', set1 | set2)
print('#2:', set1 & set2)
print('#3:', set1 - set2)
print('#4:', set1 ^ set2)
print('#5:', set1 >= set2) # false


## Question 6 
print()
def main():
    inFile = open('kings.txt', 'r')
    outFile = open('stats.txt', 'w')
    getData(inFile, outFile)
    inFile = open('stats.txt', 'r')
    display(inFile)

def getData(inFile, outFile):
    for player in inFile:
        print

def display(inFile):
    print()

main()

## Question 7

