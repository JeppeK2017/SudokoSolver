# List containg the table

table = [[None] * 9] * 9


try:
    fhand = open('sudokus/Sudoko1.txt')
except:
    print("File does not exist")
    exit()


i = 0
for line in fhand:
    for j in range(0, 9):
        table[i][j] = 0
    i = i + 1



print(table)
