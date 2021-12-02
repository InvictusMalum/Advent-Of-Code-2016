f = open("day4input.txt", "r")
input = f.read()

input = input.split("\n")


def splitRoomCode(roomCode):
    roomCode = roomCode.split('-')
    
    letters = roomCode[:len(roomCode)-1]
    splitCode = "".join(roomCode[len(roomCode)-1:]).split("[")
    sectorID = splitCode[0]
    checksum = splitCode[1]
    checksum = checksum.split("]")[0]
    letters = "".join(letters)
    
    return letters, sectorID, checksum

def processRoomCode(letters, sectorID, checksum):
    letterCounts = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letterCounts[letter] = 0
    for letter in letters:
        letterCounts[letter] += 1
    
    for i in range(len(checksum)-1):
        if letterCounts[checksum[i]] > letterCounts[checksum[i+1]]:
            pass
        elif letterCounts[checksum[i]] == letterCounts[checksum[i+1]]:
            order = sorted([checksum[i], checksum[i+1]])
            if checksum[i] == order[0]:
                pass
            else:
                return 0
        else:
            return 0
    return int(sectorID)

def processAllCodes(roomCodes):
    total = 0
    for code in roomCodes:
        letters, sectorID, checksum = splitRoomCode(code)
        total += processRoomCode(letters, sectorID, checksum)
    return total

print(processAllCodes(input))
        
            
        

        
    