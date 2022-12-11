def rock_paper_scissors(yourMove : str, theirMove : str) -> str:
    if yourMove == theirMove:
        return "Draw"
    
    elif yourMove == "Rock":
        if theirMove == "Paper":
            return "Lose"
        elif theirMove == "Scissors":
            return "Win"
    elif yourMove == "Paper":
        if theirMove == "Rock":
            return "Win"
        elif theirMove == "Scissors":
            return "Lose"
    elif yourMove == "Scissors":
        if theirMove == "Rock":
            return "Lose"
        elif theirMove == "Paper":
            return "Win"

def reverse_rock_paper_scissors(theirMove : str, outcome : str) -> str:
    if outcome == "Draw":
        return theirMove
    elif outcome == "Win":
        if theirMove == "Rock":
            return "Paper"
        elif theirMove == "Paper":
            return "Scissors"
        elif theirMove == "Scissors":
            return "Rock"
    elif outcome == "Lose":
        if theirMove == "Rock":
            return "Scissors"
        elif theirMove == "Paper":
            return "Rock"
        elif theirMove == "Scissors":
            return "Paper"

#Rock Paper Scissors
gameChoice = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

gamePoints = {
    "Rock" : 1,
    "Paper" : 2,
    "Scissors" : 3,
    "Lose" : 0,
    "Draw" : 3,
    "Win" : 6
}

if __name__ == "__main__":
    fileInput = []

    file = open("Day2Input.txt", "r")
    for line in file:
        line = line.strip()
        fileInput.append(line)
    file.close()

    #fileInput = ["A Y", "B X", "C Z"]
    totalPoints = 0

    """ Solution 1

    for game in fileInput:
        yourMove = gameChoice[game[2]]
        theirMove = gameChoice[game[0]]

        gameOutcome = rock_paper_scissors(yourMove, theirMove)
        totalPoints += gamePoints[yourMove] + gamePoints[gameOutcome]

    Solution 2"""

    for game in fileInput:
        gameOutcome = gameChoice[game[2]]
        theirMove = gameChoice[game[0]]

        yourMove = reverse_rock_paper_scissors(theirMove, gameOutcome)
        totalPoints += gamePoints[yourMove] + gamePoints[gameOutcome]

    print(totalPoints)