def read_score() -> tuple[int, int]:
    a, b = list(map(int, input().strip().split(":")))
    return a, b

def getRequiredGoals(firstScore, secondScore, gameSign):
    firstTeamGoals = firstScore[0] + secondScore[0]
    secondTeamGoals = firstScore[1] + secondScore[1]
    isCurrentGameAtHome = gameSign == 2
    firstTeamGuestScore = firstScore if isCurrentGameAtHome else secondScore
    secondTeamGuestScore = secondScore if isCurrentGameAtHome else firstScore
    goalDiff = firstTeamGoals - secondTeamGoals
    if goalDiff > 0:
        return 0
    elif goalDiff == 0:
        if firstTeamGuestScore[0] > secondTeamGuestScore[1]:
            return 0
        else:
            return 1
    else:
        if isCurrentGameAtHome:
            if firstTeamGuestScore[0] > secondTeamGuestScore[1]:
                return abs(goalDiff)
            else:
                return abs(goalDiff) + 1
        else:
            if abs(goalDiff) + secondScore[0] > secondTeamGuestScore[1]:
                return abs(goalDiff)
            return abs(goalDiff) + 1

def main():
    firstScore = read_score()
    secondScore = read_score()
    gameSign = int(input())
    print(getRequiredGoals(firstScore, secondScore, gameSign))

if __name__ == '__main__':
    main()