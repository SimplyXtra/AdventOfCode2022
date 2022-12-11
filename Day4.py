def do_zones_intersect(elfPair : list) -> bool:
    elf1Min = int(elfPair[0][0])
    elf1Max = int(elfPair[0][1])
    elf2Min = int(elfPair[1][0])
    elf2Max = int(elfPair[1][1])

    #one in two
    if elf1Min >= elf2Min and elf1Max <= elf2Max:
        return True #one is in two
    elif elf2Min >= elf1Min and elf2Max <= elf1Max:
        return True #two is in one
    else:
        return False

def do_zones_overlap(elfPair : list) -> bool:
    elf1Zones = [x for x in range(int(elfPair[0][0]), int(elfPair[0][1])+1)]
    elf2Zones = [x for x in range(int(elfPair[1][0]), int(elfPair[1][1])+1)]
    for zone in elf1Zones:
        if zone in elf2Zones:
            return True
    return False


if __name__ == "__main__":
    totalCleaningZones = []

    file = open("Day4Input.txt")
    for line in file:
        zonesInAGroup = []
        line = line.strip().split(",")
        for zones in line:
            zonesInAGroup.append(zones.split("-"))
        totalCleaningZones.append(zonesInAGroup)
    file.close()

    fullIntersections = 0

    for pair in totalCleaningZones:
        if do_zones_overlap(pair): fullIntersections += 1

    print(fullIntersections)