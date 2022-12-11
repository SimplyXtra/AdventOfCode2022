def get_points(character : str) -> str:
    if character == character.upper():
        return ord(character) - 38
    else:
        return ord(character) - 96

def intersect(setA, setB):
    return list(setA.intersection(setB))[0]

if __name__ == "__main__":
    rucksacks = []
    prioritySum = 0
    #duplicateItems = []

    file = open("Day3Input.txt")
    for line in file:
        line = line.strip()
        lineLength = len(line)
        rucksacks.append([set(line[:lineLength // 2]), set(line[lineLength // 2:])])
    file.close()

    for rucksack in rucksacks:
        prioritySum += get_points(intersect(rucksack[0], rucksack[1]))

    print(prioritySum)