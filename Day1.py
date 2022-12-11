if __name__ == "__main__":
    fileInput = [[]]

    file = open("Day1Input.txt", "r")
    i = 0
    for line in file:
        line = line.strip()
        if line == "":
            fileInput.append([])
            i += 1
        else:
            fileInput[i].append(int(line))
    del i
    file.close()



    elfCalorieCounts = []
    for CalorieCount in fileInput:
        elfCalorieCounts.append(sum(CalorieCount))
    
    topCalories = 0

    for i in range(3):
        highest = max(elfCalorieCounts)
        topCalories += highest
        elfCalorieCounts.remove(highest)

    print(topCalories)
