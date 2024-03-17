
def main():
    n = int(input())
    board = [[None] * n for _ in range(n)]
    for i in range(n):
        row, column = list(map(int, input().strip().split()))
        board[row - 1][column - 1] = 1
    print(getMinMoveCount(board, n))

def getMinMoveCount(board, n):
    filledCellsPerRow = [[] for _ in range(n)]
    filledCellsPerColumn = [0] * n
    for rowIndex, row in enumerate(board):
        for columnIndex in range(n):
            if row[columnIndex] == 1:
                filledCellsPerRow[rowIndex].append((rowIndex, columnIndex))
                filledCellsPerColumn[columnIndex] += 1
    
    rowChangingMoveCount = 0
    lastEmptyRowIndex = 0
    lastFilledRowIndex = 0
    while lastEmptyRowIndex < n:
        if len(filledCellsPerRow[lastEmptyRowIndex]) != 0:
            lastEmptyRowIndex += 1
        elif len(filledCellsPerRow[lastFilledRowIndex]) < 2:
            lastFilledRowIndex += 1
        else:
            cellToMove = filledCellsPerRow[lastFilledRowIndex].pop()
            board[cellToMove[0]][cellToMove[1]] = 0
            board[lastEmptyRowIndex][cellToMove[1]] = 1
            rowChangingMoveCount += abs(lastFilledRowIndex - lastEmptyRowIndex)
            filledCellsPerRow[lastEmptyRowIndex].append(cellToMove)
    
    columnChangingMoveCount = float("inf")
    for targetColumnIndex in range(n):
        currentColumnChangingMoveCount = 0
        for columnIndex in range(n):
            currentColumnChangingMoveCount += abs(targetColumnIndex - columnIndex) * (filledCellsPerColumn[columnIndex])
        columnChangingMoveCount = min(columnChangingMoveCount, currentColumnChangingMoveCount)
    
    return columnChangingMoveCount + rowChangingMoveCount
    
if __name__ == '__main__':
    main()   