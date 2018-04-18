a = []
try:
    lines = open('sudokus/Sudoko1.txt').read().splitlines()
except:
    print("File does not exist")
    exit()

#print(lines)
i = 0
for line in lines:
    a.append([])
    for number in line:
        a[i].append(int(number))
    i = i + 1

#print(a)




def findNextEmpty(table, posI, posJ):
    if table[posI][posJ] == 0:
        return [posI, posI]
    else:
        for j in range(posJ + 1, 9):
            if table[posI][j] == 0:
                return [posI, j]



        for i in range(posI + 1, 9):
            for j in range(0, 9):
                if table[i][j] == 0:
                    return [i,  j]
        return [-1, -1]

#print(findNextEmpty(a, 0, 0))

