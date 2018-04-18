# List containg the table


initialTable = []
solvedTable = []
try:
    lines = open('sudokus/Sudoko1.txt').read().splitlines()
except:
    print("File does not exist")
    exit()

index = 0
for line in lines:
    initialTable.append([])
    solvedTable.append([])
    for number in line:
        initialTable[index].append(int(number))
        solvedTable[index].append(int(number))
    index = index + 1



def isFull(table):
    for line in table:
        for number in line:
            if number == 0:
                return False
    return True

def findLegal(table, posI, posJ):
    curPos = table[posI][posJ]
    if curPos != 0:
        return []

    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if curPos == 0:
        for i in range(0, 9):
            #Rows
            if table[i][posJ] in possibleNumbers:
                possibleNumbers.remove(table[i][posJ])
            #Columns
            if table[posI][i] in possibleNumbers:
                possibleNumbers.remove(table[posI][i])

        for i in range((posI // 3), (posI // 3 + 3)):
            for j in range((posJ // 3), (posJ // 3 + 3)):
                if table[i][j] in possibleNumbers:
                    possibleNumbers.remove(table[i][j])

    return possibleNumbers

def isValid(table, posI, posJ, x):
    row = True
    column = True
    cell = True
    for j in range(0, 9):
        if table[posI][j] == x:
            row = False

    for i in range(0, 9):
        if table[i][posJ] == x:
            column = False

    for i in range((posI // 3 * 3), (posI // 3 * 3) + 3):
        for j in range((posJ // 3 * 3), (posJ // 3 * 3) + 3):
            if table[i][j] == x:
                cell = False
    return row and column and cell


def findNextEmpty(table, posI, posJ):
    #if table[posI][posJ] == 0:
     #   return [posI, posJ]
    #else:
        # for x in range(posI, 9):
        #     for y in range(posJ, 9):
        #         if table[x][y] == 0:
        #             return x, y
        for i in range(0, 9):
            for j in range(0, 9):
                if(table[i][j] == 0):
                    return i, j
        return -1, -1



def solver(table, posI, posJ):
    i, j = findNextEmpty(table, posI, posJ)
    if i == -1:
        return

    #legalNumbers = findLegal(table, i, j)

    for x in range(1, 10):
        if isValid(table, i, j, x):
            table[i][j] = x
            solver(table, i, j)
            if isFull(table):
                return
    table[posI][posJ] = 0


print(initialTable)
solver(solvedTable, 0, 0)
print(solvedTable)