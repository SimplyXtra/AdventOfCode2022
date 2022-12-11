def get_points(character : str) -> str:
    if character == character.upper():
        return ord(character) - 38
    else:
        return ord(character) - 96

def intersect2(setA : list, setB : list) -> list:
    intersectionSet = set(setA).intersection(set(setB))
    return list(intersectionSet)

def intersect3(setA : list, setB : list, setC : list) -> list:
    intersectionSet = set(setA).intersection(set(setB))
    intersectionSet = intersectionSet.intersection(set(setC))
    return list(intersectionSet)

if __name__ == "__main__":
    groups = []
    prioritySum = 0
    groupSize = 3


    file = open("Day3Input.txt")
    fileContent = file.readlines()
    for i in range(len(fileContent) // groupSize):
        groups.append([])
        for j in range(3):
            line = fileContent[i * groupSize + j].strip()
            groups[i].append(list(line))
            #lineLength = len(line)
            #groups[i].append([set(line[:lineLength // 2]), set(line[lineLength // 2:])])
    file.close()



    for rucksacks in groups:
        prioritySum += get_points(intersect3(rucksacks[0], rucksacks[1], rucksacks[2])[0])

    print(prioritySum)