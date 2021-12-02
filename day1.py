f = open("day1input.txt", "r")
input = f.read()
input = input.split(", ")

def countBlocks(paths):
    x = 0
    y = 0
    facing = 0
    
    for path in paths:
        turn = path[0:1]
        steps = int(path[1:])
        
        if turn == "L":
            facing = (facing+3) % 4
        elif turn == "R":
            facing = (facing+1) % 4
        
        if facing == 0:
            y += steps
        elif facing == 1:
            x += steps
        elif facing == 2:
            y -= steps
        elif facing == 3:
            x -= steps
    
    return x, y

# DOESNT WORK???
def findFirstLocateTwice(paths):
    x = 0
    y = 0
    facing = 0
    
    positions = []
    
    for path in paths:
        turn = path[0:1]
        steps = int(path[1:])
        if (x, y) in positions:
            pass
        else:
            pass
        positions.append((x,y))
        
        if turn == "L":
            facing = (facing+3) % 4
        elif turn == "R":
            facing = (facing+1) % 4

        if facing == 0:
            y += steps
        elif facing == 1:
            x += steps
        elif facing == 2:
            y -= steps
        elif facing == 3:
            x -= steps
    for position in positions:
        if position in positions[positions.index(position)+1:]:
            print(position, position[0] + position[1])
    return 0, 2
            

x, y = countBlocks(input)
print(x + y)

x2, y2 = findFirstLocateTwice(input)
print(x2, y2)
        
        
        