def isVisible(y : int, x : int) -> bool:
    global treeGrid, gridSize
    treeObserved = treeGrid[y][x]
    upClear, downClear, rightClear, leftClear = False, False, False, False
    for rowRight in range(x+1, gridSize):
        if treeGrid[y][rowRight] >= treeObserved:
            rightClear = True
            break
    for rowLeft in range(0, x):
        if treeGrid[y][rowLeft] >= treeObserved:
            leftClear = True
            break
    for columnUp in range(0, y):
        if treeGrid[columnUp][x] >= treeObserved:
            upClear = True
            break
    for columnDown in range(y+1, gridSize):
        if treeGrid[columnDown][x] >= treeObserved:
            downClear = True
            break
    
    if upClear and downClear and leftClear and rightClear:
        return False
    else:
        return True

def getSceneryScore(y : int, x : int) -> int:
    global treeGrid, gridSize
    treeObserved = treeGrid[y][x]
    upTrees = 0
    downTrees = 0
    leftTrees = 0
    rightTrees = 0

    for i in range(1, y + 1):
        upTree = treeGrid[y - i][x]
        upTrees += 1
        if upTree >= treeObserved:
            break
    for i in range(y + 1, gridSize):
        downTree = treeGrid[i][x]
        downTrees += 1
        if downTree >= treeObserved:
            break
    for i in range(1, x + 1):
        leftTree = treeGrid[y][x - i]
        leftTrees += 1
        if leftTree >= treeObserved:
            break
    for i in range(x + 1, gridSize):
        rightTree = treeGrid[y][i]
        rightTrees += 1
        if rightTree >= treeObserved:
            break

    #Debug:
    #print(upTrees)
    #print(downTrees)
    #print(leftTrees)
    #print(rightTrees)
    return upTrees * downTrees * leftTrees * rightTrees

def main():
    global treeGrid, gridSize
    with open("Day8Input.txt") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            treeGrid.append(list(map(int, line)))
        gridSize = len(treeGrid)

treeGrid = []
gridSize = 0

if __name__ == "__main__":
    main()

    """ Question 1
    visibleTrees = 0
    for y in range(gridSize):
        for x in range(gridSize):
            if isVisible(y, x): visibleTrees += 1

    print(visibleTrees)
    """
    
    #Question 2
    highestSceneryScore = 0
    for y in range(gridSize):
        for x in range(gridSize):
            highestSceneryScore = max(highestSceneryScore, getSceneryScore(y, x))
    
    print(highestSceneryScore)