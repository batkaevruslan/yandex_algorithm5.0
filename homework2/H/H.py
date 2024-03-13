
from collections import deque

def main():
    n, m = list(map(int, input().strip().split()))
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().strip().split()))
    result = getWeakestHero(board)
    print(f"{result[1][0] + 1} {result[1][1] + 1}")
#1 2
#3 4
def getStrongestHeroCells(board, forbiddenRowIndex, forbiddenColumnIndex):
    strongestHeroPower = getStrongestHeroPower(board, forbiddenRowIndex, forbiddenColumnIndex)
    strongestHeroRows = set()
    strongestHeroColumns = set()
    for rowIndex in range(len(board)):
        if rowIndex == forbiddenRowIndex:
            continue
        for columnIndex in range(len(board[0])):
            if columnIndex == forbiddenColumnIndex:
                continue
            if strongestHeroPower == board[rowIndex][columnIndex]:
                strongestHeroRows.add(rowIndex)
                strongestHeroColumns.add(columnIndex)
    return (strongestHeroRows, strongestHeroColumns)

def getStrongestHeroPower(board, forbiddenRowIndex, forbiddenColumnIndex):
    strongestHeroPower = 0
    for rowIndex in range(len(board)):
        if rowIndex == forbiddenRowIndex:
            continue
        for columnIndex in range(len(board[0])):
            if columnIndex == forbiddenColumnIndex:
                continue
            if strongestHeroPower < board[rowIndex][columnIndex]:
                strongestHeroPower = board[rowIndex][columnIndex]
    return strongestHeroPower

def getStrongestPerRow(board):
    strongestPerRow = [0] * len(board)
    for rowIndex in range(len(board)):
        strongest = 0
        for columnIndex in range(len(board[0])):
            strongest = max(strongest, board[rowIndex][columnIndex])
        strongestPerRow[rowIndex] = strongest
    return strongestPerRow

def getWeakestHero(board):
    strongestPerRow = getStrongestPerRow(board)
    strongestHeros = getStrongestHeroCells(board, None, None)
    
    weakestHero = (float("inf"), (-1, -1))
    for heroRow in strongestHeros[0]:
        strongestHerosFromForbiddenRow = getStrongestHeroCells(board, heroRow, None)
        for heroColumn in strongestHerosFromForbiddenRow[1]:
            currentHeroPower = getStrongestHeroPower(board, heroRow, heroColumn)
            weakestHeroPower = weakestHero[0]
            if currentHeroPower < weakestHeroPower:
                weakestHero = (currentHeroPower, (heroRow, heroColumn))
    
    for heroColumn in strongestHeros[1]:
        strongestHerosFromForbiddenColumn = getStrongestHeroCells(board, None, heroColumn)
        for heroRow in strongestHerosFromForbiddenColumn[0]:
            currentHeroPower = getStrongestHeroPower(board, heroRow, heroColumn)
            weakestHeroPower = weakestHero[0]
            if currentHeroPower < weakestHeroPower:
                weakestHero = (currentHeroPower, (heroRow, heroColumn))
    
    return weakestHero
if __name__ == '__main__':
    main()   