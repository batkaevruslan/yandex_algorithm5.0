import pytest
import I
import math

def test_collectsStatistics():
    statistics = I.Statistics()
    team1 = "Juventus"
    team2 = "Milan"
    inzaghi = "Inzaghi"
    delPiero = "Del Piero"
    shevchenko = "Shevchenko"

    statistics.addGame(team1, team2, [(inzaghi, 45), (delPiero, 67), (delPiero, 90)], [(shevchenko, 34)])
    assert statistics.getTotalTeamGoals(team1) == 3
    assert statistics.getTotalTeamGoals(team2) == 1
    assert math.isclose(statistics.getMeanTeamGoals(team1), 3, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanTeamGoals(team2), 1, abs_tol=0.0001)
    
    assert statistics.getTotalPlayerGoals(inzaghi) == 1
    assert statistics.getTotalPlayerGoals(delPiero) == 2
    assert statistics.getTotalPlayerGoals(shevchenko) == 1

    assert math.isclose(statistics.getMeanPlayerGoals(inzaghi), 1, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanPlayerGoals(delPiero), 2, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanPlayerGoals(shevchenko), 1, abs_tol=0.0001)

    assert statistics.getTotalPlayerGoalsOnMinute(inzaghi, 44) == 0
    assert statistics.getTotalPlayerGoalsOnMinute(inzaghi, 45) == 1

    assert statistics.getTotalPlayerGoalsOnFirstMinutes(inzaghi, 10) == 0
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 67) == 1
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 68) == 1
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 90) == 2

    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 90) == 2
    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 1) == 1
    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 45) == 2

    assert statistics.getTeamScoreOpens(team1) == 0
    assert statistics.getTeamScoreOpens(team2) == 1

    assert statistics.getPlayerScoreOpens(shevchenko) == 1
    assert statistics.getPlayerScoreOpens(inzaghi) == 0
    assert statistics.getPlayerScoreOpens(delPiero) == 0

    statistics.addGame(team1, team2, [], [])

    assert math.isclose(statistics.getMeanPlayerGoals(inzaghi), 0.5, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanPlayerGoals(delPiero), 1, abs_tol=0.0001)

    assert math.isclose(statistics.getMeanTeamGoals(team1), 1.5, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanTeamGoals(team2), 0.5, abs_tol=0.0001)

    statistics.addGame(team1, team2, [(inzaghi, 1), (delPiero, 2)], [(shevchenko, 91)])

    assert statistics.getTotalTeamGoals(team1) == 5
    assert statistics.getTotalTeamGoals(team2) == 2
    assert math.isclose(statistics.getMeanTeamGoals(team1), 1.6666, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanTeamGoals(team2), 0.6666, abs_tol=0.0001)
    
    assert statistics.getTotalPlayerGoals(inzaghi) == 2
    assert statistics.getTotalPlayerGoals(delPiero) == 3
    assert statistics.getTotalPlayerGoals(shevchenko) == 2

    assert math.isclose(statistics.getMeanPlayerGoals(inzaghi), 0.6666, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanPlayerGoals(delPiero), 1, abs_tol=0.0001)
    assert math.isclose(statistics.getMeanPlayerGoals(shevchenko), 0.6666, abs_tol=0.0001)


    assert statistics.getTotalPlayerGoalsOnMinute(inzaghi, 44) == 0
    assert statistics.getTotalPlayerGoalsOnMinute(inzaghi, 45) == 1

    assert statistics.getTotalPlayerGoalsOnFirstMinutes(inzaghi, 10) == 1
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 67) == 2
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 68) == 2
    assert statistics.getTotalPlayerGoalsOnFirstMinutes(delPiero, 90) == 3

    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 90) == 3
    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 1) == 1
    assert statistics.getTotalPlayerGoalsOnLastMinutes(delPiero, 45) == 2

    assert statistics.getTeamScoreOpens(team1) == 1
    assert statistics.getTeamScoreOpens(team2) == 1

    assert statistics.getPlayerScoreOpens(shevchenko) == 1
    assert statistics.getPlayerScoreOpens(inzaghi) == 1
    assert statistics.getPlayerScoreOpens(delPiero) == 0