from collections import deque

def main():
    m, n = list(map(int, input().strip().split()))
    board = [None] * m
    for i in range(m):
        board[i] = list(input().strip())
    result = getResult(board)
    print(result[0])
    if result[0] == "YES":
        for i in range(m):
            print("".join(result[1][i]))

class Rectangle:
    def __init__(self, topLeftColumnIndex, topLeftRowIndex, bottomRightColumnIndex = None, bottomRightRowIndex = None):
        self.topLeftColumnIndex = topLeftColumnIndex
        self.topLeftRowIndex = topLeftRowIndex
        self.bottomRightColumnIndex = bottomRightColumnIndex if bottomRightColumnIndex else topLeftColumnIndex
        self.bottomRightRowIndex = bottomRightRowIndex if bottomRightRowIndex else topLeftRowIndex

def getResult(board):
    result = areTwoRectangles(board)
    if result[0] == "NO":
        rotatedBoard = list(map(lambda x:list(x), zip(*board[::-1])))
        result = areTwoRectangles(rotatedBoard)
        if result[0] == "YES":
            result = (result[0], list(map(lambda x:list(x), zip(*result[1])))[::-1])
    return result

def areTwoRectangles(board):
    visitedCells = set()
    rectangles = []
    for rowIndex in range(len(board)):
        for columnIndex in range(len(board[0])):
            if (rowIndex, columnIndex) not in visitedCells:
                visitedCells.add((rowIndex, columnIndex))
                if board[rowIndex][columnIndex] == "#":
                    currentRectangle = Rectangle(columnIndex, rowIndex)
                    for rowIndex2 in range(rowIndex + 1, len(board)):
                        if board[rowIndex2][columnIndex] == "#":
                            visitedCells.add((rowIndex2, columnIndex))
                            currentRectangle.bottomRightRowIndex += 1
                        else:
                            break
                    if len(rectangles) == 0:
                        rectangles.append(currentRectangle)
                    else:
                        lastRectangle = rectangles[-1]
                        if ((abs(lastRectangle.topLeftColumnIndex - currentRectangle.topLeftColumnIndex) == 1 
                                or abs(lastRectangle.bottomRightColumnIndex - currentRectangle.topLeftColumnIndex) == 1)
                            and lastRectangle.bottomRightRowIndex == currentRectangle.bottomRightRowIndex
                            and lastRectangle.topLeftRowIndex == currentRectangle.topLeftRowIndex):
                            lastRectangle.bottomRightColumnIndex = currentRectangle.bottomRightColumnIndex
                        else:
                            rectangles.append(currentRectangle)
    
    if len(rectangles) == 2:
        colorBoard(board, rectangles[0], rectangles[1])
        return ("YES", board)
    elif len(rectangles) == 1:
        if rectangles[0].bottomRightColumnIndex - rectangles[0].topLeftColumnIndex > 0:
            rectangleA = Rectangle(rectangles[0].topLeftColumnIndex, rectangles[0].topLeftRowIndex, rectangles[0].topLeftColumnIndex, rectangles[0].bottomRightRowIndex)
            rectangleB = Rectangle(rectangles[0].topLeftColumnIndex + 1, rectangles[0].topLeftRowIndex, rectangles[0].bottomRightColumnIndex, rectangles[0].bottomRightRowIndex)
            colorBoard(board, rectangleA, rectangleB)
            return ("YES", board)
        elif rectangles[0].bottomRightRowIndex - rectangles[0].topLeftRowIndex > 0:
            rectangleA = Rectangle(rectangles[0].topLeftColumnIndex, rectangles[0].topLeftRowIndex, rectangles[0].bottomRightColumnIndex, rectangles[0].topLeftRowIndex)
            rectangleB = Rectangle(rectangles[0].topLeftColumnIndex, rectangles[0].topLeftRowIndex + 1, rectangles[0].bottomRightColumnIndex, rectangles[0].bottomRightRowIndex)
            colorBoard(board, rectangleA, rectangleB)
            return ("YES", board)
        
    return ("NO", None)

def colorBoard(board, rectangleA, rectangleB):
    for rowIndex in range(rectangleA.topLeftRowIndex, rectangleA.bottomRightRowIndex + 1):
        for columnIndex in range(rectangleA.topLeftColumnIndex, rectangleA.bottomRightColumnIndex + 1):
            board[rowIndex][columnIndex] = "a"
    
    for rowIndex in range(rectangleB.topLeftRowIndex, rectangleB.bottomRightRowIndex + 1):
        for columnIndex in range(rectangleB.topLeftColumnIndex, rectangleB.bottomRightColumnIndex + 1):
            board[rowIndex][columnIndex] = "b"

if __name__ == '__main__':
    main()   