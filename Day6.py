def isUnique(array : list) -> bool:
    for i in array:
        if array.count(i) > 1: return False
    return True

def findUniqueMarker(data : str, length : int) -> str and int:
    marker = ""
    for i in range(len(data)):
        marker += data[i]
        if i >= length:
            marker = marker[1:]
            if isUnique(marker):
                return(marker, i + 1)

if __name__ == "__main__":
    
    file = open("Day6Input.txt")
    data = file.read().strip()
    file.close()

    packetMarker, markerPosition = findUniqueMarker(data, 14)
    print(markerPosition)
    