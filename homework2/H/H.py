
from collections import deque


def main():
    n, m = list(map(int, input().strip().split()))
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().strip().split()))
    result = getWeakestHero(board, None, None)
    print(f"{result[1][0] + 1} {result[1][1] + 1}")
#1 2
#3 4
def getWeakestHero(board, forbiddenRowIndex, forbiddenColumnIndex):
    strongestHero = 0
    strongestHeroCells = deque()
    for rowIndex in range(len(board)):
        if rowIndex == forbiddenRowIndex:
            continue
        for columnIndex in range(len(board[0])):
            if columnIndex == forbiddenColumnIndex:
                continue
            if strongestHero < board[rowIndex][columnIndex]:
                strongestHero = board[rowIndex][columnIndex]
                strongestHeroCells.clear()
                strongestHeroCells.append((rowIndex, columnIndex))
            elif strongestHero == board[rowIndex][columnIndex]:
                strongestHeroCells.append((rowIndex, columnIndex))
    
    if forbiddenColumnIndex != None and forbiddenRowIndex != None:
        return (strongestHero, (forbiddenRowIndex, forbiddenColumnIndex))
    
    weakestHero = (float("inf"), (-1, -1))
    if forbiddenRowIndex == None:
        forbiddenRowIndicies = set()
        for heroCell in strongestHeroCells:
            if heroCell[0] not in forbiddenRowIndicies:
                forbiddenRowIndicies.add(heroCell[0])
                currentWeakHero = getWeakestHero(board, heroCell[0], forbiddenColumnIndex)
                if currentWeakHero[0] < weakestHero[0]:
                    weakestHero = currentWeakHero
    if forbiddenColumnIndex == None:
        forbiddenColumnIndex = set()
        for heroCell in strongestHeroCells:
            if heroCell[1] not in forbiddenColumnIndex:
                forbiddenColumnIndex.add(heroCell[1])
                currentWeakHero = getWeakestHero(board, forbiddenRowIndex, heroCell[1])
                if currentWeakHero[0] < weakestHero[0]:
                    weakestHero = currentWeakHero
    
    return weakestHero
if __name__ == '__main__':
    main()   