def translateInstructions(instructions : list) -> str:
    finalInstructions = []
    for instruction in instructions:
        bareInstructions = instruction.split()
        splitInstructions = []
        for word in bareInstructions:
            if word.isnumeric():
                splitInstructions.append(int(word))
        finalInstructions.append(splitInstructions)
    return finalInstructions

def translateStacks(cellSize : int, rawStacks : list) -> list:
    orderedStacks = []
    noOfStacks = len(rawStacks[0]) // cellSize
    
    #Get 2D Array
    for i in range(noOfStacks):
        orderedStacks.append([])
    
    for row in range(len(rawStacks)): #Rows
        for column in range(noOfStacks): #Columns
            crate = rawStacks[row][column*cellSize:(column+1)*cellSize][1] #Gets second character of cell in position j
            if crate != " ":
                orderedStacks[column].append(crate)
    
    return orderedStacks

def sortWithCrateMover9000(stacks: list, instruction : list) -> list:
    noOfCrates, startingStack, endingStack = instruction
    for i in range(noOfCrates):
        movingCrate = stacks[startingStack-1][0]
        stacks[startingStack-1].pop(0)
        stacks[endingStack-1].insert(0, movingCrate)
    return stacks

def sortWithCrateMover9001(stacks: list, instruction : list) -> list:
    noOfCrates, startingStack, endingStack = instruction
    movingCrates = stacks[startingStack-1][:noOfCrates]
    del stacks[startingStack-1][:noOfCrates]
    movingCrates.extend(stacks[endingStack-1])
    stacks[endingStack-1] = movingCrates
    return stacks

if __name__ == "__main__":
    #Variables
    rawStacks = []
    rawInstructions = []
    cellSize = 4

    #Read Data
    file = open("Day5Input.txt")
    isFilePastOrder = False
    for line in file:
        if line.strip() == "":
            isFilePastOrder = True
        if not isFilePastOrder:
            rawStacks.append(line)
        else:
            rawInstructions.append(line.strip())
    rawInstructions.pop(0)
    rawStacks.pop(-1)
    del isFilePastOrder
    file.close()

    stacks = translateStacks(cellSize, rawStacks)
    stackInstructions = translateInstructions(rawInstructions)

    for instruction in stackInstructions:
        #stacks = sortWithCrateMover9000(stacks, instruction)
        stacks = sortWithCrateMover9001(stacks, instruction)
    
    for stack in stacks:
        print(stack[0], end = "")
