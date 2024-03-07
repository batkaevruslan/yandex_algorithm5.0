def getUnreachableCellCount(board):
    boardSize = 8
    for rowIndex in range(boardSize):
        for columnIndex in range(boardSize):
            if board[rowIndex][columnIndex] == 'R':
                visitBoard(board, rowIndex, columnIndex, (1, 0))
                visitBoard(board, rowIndex, columnIndex, (-1, 0))
                visitBoard(board, rowIndex, columnIndex, (0, 1))
                visitBoard(board, rowIndex, columnIndex, (0, -1))
            elif board[rowIndex][columnIndex] == 'B':
                visitBoard(board, rowIndex, columnIndex, (1, 1))
                visitBoard(board, rowIndex, columnIndex, (1, -1))
                visitBoard(board, rowIndex, columnIndex, (-1, -1))
                visitBoard(board, rowIndex, columnIndex, (-1, 1))
    
    result = 0
    for rowIndex in range(boardSize):
        for columnIndex in range(boardSize): 
            if board[rowIndex][columnIndex] == "*":
                result += 1
    return result

def visitBoard(board, rowStartIndex, columnStartIndex, direction: tuple[int, int]):
    rowIndex = rowStartIndex + direction[0]
    columnIndex = columnStartIndex + direction[1]
    while (rowIndex >= 0 
           and rowIndex < len(board) 
           and columnIndex >= 0 
           and columnIndex < len(board[0])
           and board[rowIndex][columnIndex] != 'R'
           and board[rowIndex][columnIndex] != 'B'):
        board[rowIndex][columnIndex] = '#'
        rowIndex += direction[0]
        columnIndex += direction[1]

def main():
    boardSize = 8
    board = [["*"] * boardSize for _ in range(boardSize)]
    for i in range(boardSize):
        line = input()
        for j in range(boardSize):
            board[i][j] = line[j]
    print(getUnreachableCellCount(board))

if __name__ == '__main__':
    main()