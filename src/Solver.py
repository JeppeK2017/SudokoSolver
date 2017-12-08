# List containg the table

import os

try:
    lines = open('sudokus/Sudoko1.txt').read().splitlines()
except:
    print("File does not exist")
    exit()
table = lines
finishedTable = lines



def findLegal(table, posI, posJ):
    print("Find legal method")
    test = int(table[posI][posJ])

    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if test == 0:
        #Rows
        for j in range(0, 9):
            if j != posJ:
                val = int(table[posI][j])
                if val != 0 and possibleNumbers.count(val) != 0:
                    possibleNumbers.remove(val)

        #Columns
        for i in range(0, 9):
            if i != posI:
                val = int(table[i][posJ])
                if val != 0 and possibleNumbers.count(val) != 0:
                    possibleNumbers.remove(val)

        # 3x3 square
        if posI < 3:
            if posJ < 3:
                #First square row 1 col 2
                for i in range(0, 3):
                    for j in range(0, 3):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)

            elif posJ >= 6:
                #Second square row 1 col 3
                for i in range(0, 3):
                    for j in range(6, 9):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)

            else:
                #Third square row 1 col 2
                for i in range(0, 3):
                    for j in range(3, 5):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)

        elif posI >= 6:
            if posJ < 3:
                #First square row 3 col 2
                for i in range(6, 9):
                    for j in range(0, 3):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)
            elif posJ >= 6:
                #Second square row 3 col 3
                for i in range(6, 9):
                    for j in range(6, 9):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)
            else:
                #Third square row 3 col 2
                for i in range(6, 9):
                    for j in range(3, 6):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)

        else:
            if posJ < 3:
                #First square row 2 col 1
                for i in range(3, 6):
                    for j in range(0, 3):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)
            elif posJ >= 6:
                #Second square row 2 col 3
                for i in range(3, 6):
                    for j in range(6, 9):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)
            else:
                #Third square row 2 col 2
                for i in range(3, 6):
                    for j in range(3, 6):
                        if i != posI and j != posJ:
                            val = int(table[i][posJ])
                            if val != 0 and possibleNumbers.count(val) != 0:
                                possibleNumbers.remove(val)



    return possibleNumbers


for i in range(0, 9):
    for j in range(0, 9):
        print(findLegal(table, i, j))

