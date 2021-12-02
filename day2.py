f = open("day2input.txt", "r")
input = f.read()

directions = input.split("\n")

def findCode(direction, row, col):
    for dirChar in direction:
        if dirChar == "U":
            row = max(0,min(row - 1, 2))
        elif dirChar == "R":
            col = max(0,min(col + 1, 2))
        elif dirChar == "D":
            row = max(0,min(row + 1, 2))
        elif dirChar == "L":
            col = max(0,min(col - 1, 2))
    return row, col


map = [
['0','0','1','0','0','0'],
['0','2','3','4','0','0'],
['5','6','7','8','9','0'],
['0','A','B','C','0','0'],
['0','0','D','0','0','0'],
['0','0','0','0','0','0']]
def findCodeInMap(direction, row, col, map):
    for dirChar in direction:
        if dirChar == "U":
            if map[row-1][col] != '0':
                row = row-1
        elif dirChar == "R":
            if map[row][col+1] != '0':
                col = col+1
        elif dirChar == "D":
            if map[row+1][col] != '0':
                row = row+1
        elif dirChar == "L":
            if map[row][col-1] != '0':
                col = col-1
    return row, col

# Part 1
row = 1
col = 1
out = []
for i in range(5):
    row, col = findCode(directions[i],row,col)
    out.append(row*3+col+1)
print(out)

# Part 2
row = 2
col = 0
out = []
for i in range(5):
    row, col = findCodeInMap(directions[i],row,col,map)
    out.append(map[row][col])
print(out)
