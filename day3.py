f = open("day3input.txt", "r")
input = f.read()

def isValidTriangle(sides):
    if sides[1] + sides[2] <= sides[0]:
        return False
    if sides[0] + sides[2] <= sides[1]:
        return False
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True

def countAllValidTriangles(triangles):
    triangles = triangles.split("\n")
    total = 0
    for triangle in triangles:
        sides = triangle.split(" ")[1:]
        realSides = []
        for i in range(len(sides)):
            if sides[i] != '':
                realSides.append(int(sides[i]))
                
        if isValidTriangle(realSides):
            total += 1
    return total

def countAllValidTrianglesInCols(triangles):
    total = 0
    
    #Convert Rows to integers
    rows = triangles.split("\n")
    for i in range(len(rows)):
        intRow = []
        strings = rows[i].split(" ")
        for string in strings:
            if string != '':
                intRow.append(int(string))
        rows[i] = intRow
    
    #
    for rowIndex in range(0,len(rows),3):
        tri1 = [rows[rowIndex][0], rows[rowIndex+1][0], rows[rowIndex+2][0]]
        tri2 = [rows[rowIndex][1], rows[rowIndex+1][1], rows[rowIndex+2][1]]
        tri3 = [rows[rowIndex][2], rows[rowIndex+1][2], rows[rowIndex+2][2]]
        for tri in [tri1, tri2, tri3]:
            if isValidTriangle(tri):
                total += 1
    return total

print(countAllValidTriangles(input))
print(countAllValidTrianglesInCols(input))