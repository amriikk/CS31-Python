##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch7_HW
# Due Date: 05.01.21
# ####################################################

## Problems 11 - Lo Shu Magic Square
def main():
    matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    loShu(matrix)


def loShu(matrix):

    i = 0
    j = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[j])):
            if ((matrix[i][j] < 1) or (matrix[i][j] > 9)):
                return ('This is not a Lo Shu Magic Square - one of the numbers is invalid')

    row1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
    row2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
    row3 = matrix[2][0] + matrix[2][1] + matrix[2][2]

    col1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
    col2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
    col3 = matrix[0][2] + matrix[1][2] + matrix[2][2]

    diag1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    diag2 = matrix[0][2] + matrix[1][1] + matrix[2][0]

    checkList = [row1,row2,row3,col1,col2,col3,diag1,diag2]

    temp = checkList[0]

    for x in range (0, len(checkList)):
        if checkList[x] != temp:
            return ('This is not a Lo Shu Magic Square')

    return ('This is a Lo Shu Magic Square')


main()
