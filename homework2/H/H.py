
from datetime import datetime

def main():
    """n, m = list(map(int, input().strip().split()))
    board = [[0] * m for _ in range(n)]
    board = [[float("-inf")] * (m +2) for _ in range(n + 2)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            board[i + 1][j + 1] = row[j]"""
    print(datetime.now())
    reader = open('input.txt', 'r')
    n, m = list(map(int, reader.readline().strip().split()))
    board = [[float("-inf")] * (m +2) for _ in range(n + 2)]
    for i in range(n):
        row = list(map(int, reader.readline().split()))
        for j in range(m):
            board[i + 1][j + 1] = row[j]
    reader.close()
    print(datetime.now())
    result = getWeakestHero(board, n, m)
    print(datetime.now())
    print(f"{result[0]} {result[1]}")

def getWeakestHero(board, rowCount, columnCount):
    maxPowerData = []
    topLeftBoard = getBoardOfMaximums(board, 1, 1, 1, 1, maxPowerData)
    print(datetime.now())
    topRightBoard = getBoardOfMaximums(board, 1, columnCount, 1, -1)
    print(datetime.now())
    bottomLeftBoard = getBoardOfMaximums(board, rowCount, 1, -1, 1)
    print(datetime.now())
    bottomRightBoard = getBoardOfMaximums(board, rowCount, columnCount, -1, -1)
    print(datetime.now())

    weakestHeroPower = float("inf")
    for rowIndex in range(1, rowCount + 1):
        for columnIndex in range(1, columnCount +1):
            tRowIndex = rowIndex - 1
            tColumnIndex = columnIndex - 1
            topLeftZoneStrongestPower = topLeftBoard[tRowIndex][tColumnIndex]
            
            tRowIndex = rowIndex - 1
            tColumnIndex = columnIndex + 1
            topRightZoneStorngestPower = topRightBoard[tRowIndex][tColumnIndex]
            
            tRowIndex = rowIndex + 1
            tColumnIndex = columnIndex - 1
            bottomLeftZoneStrongestPower = bottomLeftBoard[tRowIndex][tColumnIndex]
            
            tRowIndex = rowIndex + 1
            tColumnIndex = columnIndex + 1
            bottomRightZoneStrongestPower = bottomRightBoard[tRowIndex][tColumnIndex]
            strongestHeroPower = max(topLeftZoneStrongestPower, topRightZoneStorngestPower, bottomLeftZoneStrongestPower, bottomRightZoneStrongestPower)
            if strongestHeroPower < weakestHeroPower:
                weakestHeroPower = strongestHeroPower
                forbiddenRowIndex = rowIndex
                forbiddenColumnIndex = columnIndex
    
    return (forbiddenRowIndex, forbiddenColumnIndex)

def getWeakestHeroFromBoardOfMaximums(boardOfMaximums, rowIndex, columnIndex, rowCount, columnCount):
    if rowIndex < 0 or rowIndex >= rowCount or columnIndex < 0 or columnIndex >= columnCount:
        return float("-inf")
    return boardOfMaximums[rowIndex][columnIndex]

def getBoardOfMaximums(board, rowStartIndex, columnStartIndex, rowShift, columnShift, maxPowerdata = None):
    maxPower = float("-inf")
    maxPowerRowIndex = -1
    maxPowerClumnIndex = -1

    rowCount = len(board) - 1
    columnCount = len(board[0]) - 1

    rowEndIndex = 0 if rowShift < 0 else rowCount
    columnEndIndex = 0 if columnShift < 0 else columnCount

    neigborRowIndexShift = rowShift * -1
    neigborColumnIndexShift = columnShift * -1
    boardOfMaximums = [[0] * len(board[0]) for _ in range(len(board))]

    for rowIndex in range(rowStartIndex, rowEndIndex, rowShift):
        for columnIndex in range(columnStartIndex, columnEndIndex, columnShift):
            rowNeigborRowIndex = rowIndex + neigborRowIndexShift
            columnNeigborColumnIndex = columnIndex + neigborColumnIndexShift
            rowNeigborPower = boardOfMaximums[rowNeigborRowIndex][columnIndex]# if 0 <= rowNeigborRowIndex and rowNeigborRowIndex < rowCount else float("-inf")
            columnNeigborPower = boardOfMaximums[rowIndex][columnNeigborColumnIndex]# if 0 <= columnNeigborColumnIndex and columnNeigborColumnIndex < columnCount else float("-inf")
            currentCellPower = board[rowIndex][columnIndex]
            boardOfMaximums[rowIndex][columnIndex] = max(currentCellPower, rowNeigborPower, columnNeigborPower)
            
            #if maxPowerdata != None and board[rowIndex][columnIndex]
    
    return boardOfMaximums


if __name__ == '__main__':
    main()   