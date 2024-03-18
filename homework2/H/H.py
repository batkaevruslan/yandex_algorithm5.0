
from collections import deque

def main():
    """n, m = list(map(int, input().strip().split()))
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().strip().split()))"""
    reader = open('input.txt', 'r')
    n, m = list(map(int, reader.readline().strip().split()))
    board = [[float("-inf")] * (m) for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, reader.readline().split()))
    reader.close()
    result = getWeakestHero(board)
    print(f"{result[1][0] + 1} {result[1][1] + 1}")
#1 2
#3 4
def getStrongestHeroCells(board, forbiddenRowIndex, forbiddenColumnIndex):
    strongestHero = 0
    strongestHeroCells = []
    for rowIndex in range(len(board)):
        if rowIndex == forbiddenRowIndex:
            continue
        for columnIndex in range(len(board[0])):
            if columnIndex == forbiddenColumnIndex:
                continue
            if strongestHero < board[rowIndex][columnIndex]:
                strongestHero = board[rowIndex][columnIndex]
                strongestHeroCells = [(rowIndex, columnIndex)]
    return strongestHeroCells

def getWeakestHero(board):
    strongestHeroCells = getStrongestHeroCells(board, None, None)
    
    weakestHero = (float("inf"), (-1, -1))
    forbiddenRowIndicies = set()
    for heroCell in strongestHeroCells:
        if heroCell[0] not in forbiddenRowIndicies:
            forbiddenRowIndicies.add(heroCell[0])
            strongestHerosFromForbiddenRow = getStrongestHeroCells(board, heroCell[0], None)
            for heroFromForbiddenRow in strongestHerosFromForbiddenRow:
                strongestHerosFromForbiddenRowAndColumn = getStrongestHeroCells(board, heroCell[0], heroFromForbiddenRow[1])
                for currentWeakHero in strongestHerosFromForbiddenRowAndColumn:
                    currentHeroPower = board[currentWeakHero[0]][currentWeakHero[1]]
                    weakestHeroPower = weakestHero[0]
                    if currentHeroPower < weakestHeroPower:
                        weakestHero = (board[currentWeakHero[0]][currentWeakHero[1]], (heroCell[0], heroFromForbiddenRow[1]))
    
    forbiddenColumnIndex = set()
    for heroCell in strongestHeroCells:
        if heroCell[1] not in forbiddenColumnIndex:
            forbiddenColumnIndex.add(heroCell[1])
            strongestHerosFromForbiddenColumn = getStrongestHeroCells(board, None, heroCell[1])
            for heroFromForbiddenColumn in strongestHerosFromForbiddenColumn:
                strongestHerosFromForbiddenRowAndColumn = getStrongestHeroCells(board, heroFromForbiddenColumn[0], heroCell[1])
                for currentWeakHero in strongestHerosFromForbiddenRowAndColumn:
                    currentHeroPower = board[currentWeakHero[0]][currentWeakHero[1]]
                    weakestHeroPower = weakestHero[0]
                    if currentHeroPower < weakestHeroPower:
                        weakestHero = (board[currentWeakHero[0]][currentWeakHero[1]], (heroFromForbiddenColumn[0], heroCell[1]))
    
    return weakestHero
if __name__ == '__main__':
    main()   