def main():
    n = int(input())
    board = [[False] * 8 for _ in range(8)]
    for _ in range(n):
        rowNum, columnNum =  list(map(int, input().strip().split()))
        board[rowNum - 1][columnNum - 1] = True

    print(getPerimeter(board))

def getPerimeter(board):
    perimeter = 0
    for rowIndex in range(8):
        for columnIndex in range(8):
            if board[rowIndex][columnIndex]:
                if columnIndex == 0 or board[rowIndex][columnIndex - 1] == False:
                    perimeter += 1 #left
                if columnIndex == 7 or board[rowIndex][columnIndex + 1] == False:
                    perimeter += 1 #right
                if rowIndex == 0 or board[rowIndex - 1][columnIndex] == False:
                    perimeter += 1 #top
                if rowIndex == 7 or board[rowIndex + 1][columnIndex] == False:
                    perimeter += 1
    return perimeter   

if __name__ == '__main__':
    main()    