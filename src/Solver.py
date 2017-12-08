# List containg the table

import os

try:
    lines = open('sudokus/Sudoko1.txt').read().splitlines()
except:
    print("File does not exist")
    exit()
table = lines



def findLegal(table, posI, posJ):
    print("Find legal method")
    test = int(table[posI][posJ])

    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if test == 0:
        #Rows
        for j in range(0, 9):
            if j != posJ:
                val = int(table[posI][j])
                if val != 0:
                    possibleNumbers.remove(val)

        #Columns
        for i in range(0, 9):
            if i != posI:
                val = int(table[i][posJ])
                if val != 0:
                    possibleNumbers.remove(val)

        # 3x3 square

    return possibleNumbers


legalNumbers = findLegal(table, 0, 0)
print(legalNumbers)
