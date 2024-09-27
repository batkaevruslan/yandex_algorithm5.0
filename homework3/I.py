class Statistics:
    def __init__(self):
        self.team1LeftGoals = 0
        self.team2LeftGoals = 0
        self.totalGoalsByTeam = {}
        self.totalGamesByTeam = {}
        self.scoreOpensByTeam = {}
        self.scoreOpensByPlayer = {}
        self.totalGoalsByPlayer = {}
        self.goalByMinuteByPlayer = {}
        self.teamByPlayer = {}
    
    def addGame(self, team1, team2, goals1, goals2):
        self.__addGame(team1, len(goals1))
        self.__addGame(team2, len(goals2))

        if len(goals1) > 0 or len(goals2) > 0:
            firstScoreMinute1 = self.__collectGoalStatistics(team1, goals1)
            firstScoreMinute2 = self.__collectGoalStatistics(team2, goals2)
            
            openScoreTeam = team1 if firstScoreMinute1[0] < firstScoreMinute2[0] else team2
            openScorePlayer = firstScoreMinute1[1] if firstScoreMinute1[0] < firstScoreMinute2[0] else firstScoreMinute2[1]
            self.scoreOpensByTeam.setdefault(openScoreTeam, 0)
            self.scoreOpensByTeam[openScoreTeam] += 1
            self.scoreOpensByPlayer.setdefault(openScorePlayer, 0)
            self.scoreOpensByPlayer[openScorePlayer] += 1
    
    def getTotalTeamGoals(self, team):
        return self.totalGoalsByTeam.setdefault(team, 0)
    
    def getMeanTeamGoals(self, team):
        return self.totalGoalsByTeam[team] / self.totalGamesByTeam[team]
    
    def getTotalPlayerGoals(self, player):
        return self.totalGoalsByPlayer.setdefault(player, 0)
    
    def getMeanPlayerGoals(self, player):
        playerTeam = self.teamByPlayer[player]
        return self.totalGoalsByPlayer[player] / self.totalGamesByTeam[playerTeam]
    
    def getTotalPlayerGoalsOnMinute(self, player, minute):
        goalByMinute = self.goalByMinuteByPlayer.setdefault(player, {})
        return goalByMinute.setdefault(minute, 0)
    
    def getTotalPlayerGoalsOnFirstMinutes(self, player, minutes):
        totalGoals = 0
        for minute in range(1, minutes + 1):
            totalGoals += self.getTotalPlayerGoalsOnMinute(player, minute)
        return totalGoals
    
    def getTotalPlayerGoalsOnLastMinutes(self, player, minutes):
        totalGoals = 0
        for minute in range(91 - minutes, 91):
            totalGoals += self.getTotalPlayerGoalsOnMinute(player, minute)
        return totalGoals
    
    def getTeamScoreOpens(self, team):
        return self.scoreOpensByTeam.setdefault(team, 0)
    
    def getPlayerScoreOpens(self, player):
        return self.scoreOpensByPlayer.setdefault(player, 0)
    
    def __collectGoalStatistics(self, team, goals):
        minMinute = 90
        firstScorePlayer = ""
        for goal in goals:
            minute = goal[1]
            player = goal[0]
            self.__addPlayerGoal(player, minute)
            if minute < minMinute:
                minMinute = minute
                firstScorePlayer = player

            self.teamByPlayer[player] = team
        return (minMinute, firstScorePlayer)
    
    def __addPlayerGoal(self, player, minute):
        minute = min(90, minute)
        self.totalGoalsByPlayer.setdefault(player, 0)
        self.totalGoalsByPlayer[player] += 1
        
        goalByMinute = self.goalByMinuteByPlayer.setdefault(player, {})
        goalByMinute.setdefault(minute, 0)
        goalByMinute[minute] += 1

    def __addGame(self, team, goals):
        teamCurrentTotal = self.totalGoalsByTeam.setdefault(team, 0)
        self.totalGoalsByTeam[team] = teamCurrentTotal + goals

        self.totalGamesByTeam.setdefault(team, 0)
        self.totalGamesByTeam[team] += 1
    

def main():
    statistics = Statistics()
    reader = open('input.txt', "r")
    line = reader.readline()
    while line != "":
        if "-" in line:
            parts = line.split("\"")
            team1 = parts[1].strip('"')
            team2 = parts[3].strip('"')
            scorePart = parts[4]
            team1Score, team2Score = list(map(int, scorePart.split(":")))
            goals1 = []
            for _ in range(team1Score):
                parts = reader.readline().split()
                minute = int(parts[-1].rstrip("'"))
                player = " ".join(parts[0:len(parts)-1])
                goals1.append((player, minute))
            goals2 = []
            for _ in range(team2Score):
                parts = reader.readline().split()
                minute = int(parts[-1].rstrip("'"))
                player = " ".join(parts[0:len(parts)-1])
                goals2.append((player, minute))
            statistics.addGame(team1, team2, goals1, goals2)
        elif line.startswith("Total goals for \""):
            firstIndex = len("Total goals for \"")
            team = line[firstIndex:len(line) - 1].strip('"')
            print(statistics.getTotalTeamGoals(team))
        elif line.startswith("Mean goals per game for \""):
            firstIndex = len("Mean goals per game for \"")
            team = line[firstIndex:len(line) - 1].strip('"')
            print(statistics.getMeanTeamGoals(team))
        elif  line.startswith("Total goals by "):
            firstIndex = len("Total goals by ")
            player = line[firstIndex: len(line) - 1]
            print(statistics.getTotalPlayerGoals(player))
        elif line.startswith("Mean goals per game by "):
            firstIndex = len("Mean goals per game by ")
            player = line[firstIndex: len(line) - 1]
            print(statistics.getMeanPlayerGoals(player))
        elif line.startswith("Goals on minute "):
            firstIndex = len("Goals on minute ")
            suffix = line[firstIndex: len(line) - 1]
            minuteStr, player = suffix.split(" by ")
            print(statistics.getTotalPlayerGoalsOnMinute(player.strip(), int(minuteStr)))
        elif line.startswith("Goals on first "):
            firstIndex = len("Goals on first ")
            suffix = line[firstIndex: len(line) - 1]
            minuteStr, player = suffix.split(" minutes by ")
            print(statistics.getTotalPlayerGoalsOnFirstMinutes(player.strip(), int(minuteStr)))
        elif line.startswith("Goals on last "):
            firstIndex = len("Goals on last ")
            suffix = line[firstIndex: len(line) - 1]
            minuteStr, player = suffix.split(" minutes by ")
            print(statistics.getTotalPlayerGoalsOnLastMinutes(player.strip(), int(minuteStr)))
        elif line.startswith("Score opens by \""):
            firstIndex = len("Score opens by \"")
            team = line[firstIndex:len(line) - 1].strip('"')
            print(statistics.getTeamScoreOpens(team))
        elif line.startswith("Score opens by "):
            firstIndex = len("Score opens by ")
            player = line[firstIndex: len(line) - 1]
            print(statistics.getPlayerScoreOpens(player))
        line = reader.readline()

    reader.close()
    #result = getMoveCount(linesA, linesB)
    #print(result)

if __name__ == '__main__':
    main()   