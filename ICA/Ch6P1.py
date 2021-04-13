# Week 10, ICA 1

outfile = open('players.txt', 'w')
outfile.write('Sidney Crosbly'+'\n')
outfile.write('John Carlson'+'\n')
outfile.write('Jordan Binnington'+'\n')
outfile.close()
# Append one more name in the file
outfile = open('players.txt','a')
outfile.write('Alex Ovechkin\n')
outfile.close()
outfile = open('numbers.txt','w')
outfile.write(str(89)+'\n')
outfile.write(str(74)+'\n')
outfile.write(str(50)+'\n')
outfile.write(str(8)+'\n')
outfile.close()
# Create input file object
infile1 = open('players.txt','r')
infile2 = open('numbers.txt','r')
player = infile1.readline().rstrip('\n')
num = infile2.readline().rstrip('n')
while player != '' and num != '':
    print(player,'wears number',num)
# # Read player names from file
# player1 = infile1.readline()
# player1 = player1.rstrip('\n')
# player2 = infile1.readline().rstrip('\n')
# player3 = infile1.readline().rstrip('\n')
# player4 = infile1.readline().rstrip('\n')
# # Read numbers from file
# infile2 = open('numbers.txt','r')
# num1 = infile2.readline().rstrip('\n')
# num2 = infile2.readline().rstrip('\n')
# num3 = infile2.readline().rstrip('\n')
# num4 = infile2.readline().rstrip('\n')
# # Output and close file objects
# print(player1, num1)
# print(player2, num2)
# print(player3, num3)
# print(player4, num4)
infile1.close()
infile2.close()