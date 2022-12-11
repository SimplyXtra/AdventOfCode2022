def readFile() -> list:
    
    def exitIndex(index : str):
        if index != "":
            store = index.split("/")
            store.pop(-1)
            store.pop(-1)
            newIndex = ""
            for fileName in store:
                newIndex += fileName + "/"
            index = newIndex
        return index

    systemData = ["."]
    index = "./"
    isAddingFiles = False

    file = open("Day7Input.txt")
    for line in file:
        data = line.strip().split()
        if data[0] == "$":
            if data[1] == "cd":
                isAddingFiles = False
                if data[2] == "/":
                    index = "./"
                elif data[2] == "..":
                    index = exitIndex(index)
                else:
                    if systemData.count(index + data[2]) > 0:
                        index += data[2] + "/"
        if data[0] == "dir" and systemData.count(index + data[1]) < 1:
            systemData.append(index + data[1])
        elif systemData.count(index + data[0]) < 1:
            systemData.append(index + data[0])
        

    #systemData[0] = systemData[0][:-1]

    systemData.sort()
    return systemData

if __name__ == "__main__":
    system = readFile()

    directorySizes = {}

    for fileName in system:
        if not fileName[-1].isnumeric():
            directorySizes.update({fileName : 0})

    for fileName in system:
        for directory in directorySizes:
            if fileName[-1].isnumeric() and fileName.startswith(directory):
                noOfBits = fileName.split("/")[-1]
                directorySizes[directory] += int(noOfBits)
    
    #Question 1
    sumOfSmallDirectories = 0

    for directory in directorySizes:
        if directorySizes[directory] <= 100000:
            sumOfSmallDirectories += directorySizes[directory]

    #Question 2
    totalDiskSpace = 70000000
    updateSpace = 30000000
    requiredSpace = directorySizes["."] + 30000000 - totalDiskSpace

    smallestDirectoryBigEnough = totalDiskSpace

    for directory in directorySizes:
        if directorySizes[directory] > requiredSpace:
            smallestDirectoryBigEnough = min(smallestDirectoryBigEnough, directorySizes[directory])
    
    print(smallestDirectoryBigEnough)