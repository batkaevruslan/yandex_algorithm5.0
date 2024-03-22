from collections import deque
from typing import List

    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented
    
    def __repr__(self):
        return str(f"({self.x};{self.y})")
    
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start if start.x < end.x else end
        self.end = end if start.x < end.x else start

    def __key(self):
        return (self.start, self.end)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Line):
            return self.__key() == other.__key()
        return NotImplemented
    
    def __repr__(self):
        return str(f"({self.start}-{self.end})")
    
def main():
    reader = open('input.txt', 'r')
    n = int(reader.readline())
    linesA = []
    for _ in range(n):
        x1, y1, x2, y2 = list(map(int, reader.readline().strip().split()))
        startPoint = Point(x1, y1)
        endPoint = Point(x2, y2)
        linesA.append(Line(startPoint, endPoint))
    
    linesB = []
    for _ in range(n):
        x1, y1, x2, y2 = list(map(int, reader.readline().strip().split()))
        startPoint = Point(x1, y1)
        endPoint = Point(x2, y2)
        linesB.append(Line(startPoint, endPoint))
    reader.close()

    result = getMoveCount(linesA, linesB)
    print(result)

def getMoveCount(linesA: List[Line], linesB:List[Line]):
    bestMoveCount = len(linesA)
    bestMoveByShift = {}
    bSet = set(linesB)
    for lineA in linesA:
        for lineB in linesB:
            shiftX1 = lineB.start.x - lineA.start.x
            shiftY1 = lineB.start.y - lineA.start.y
            shiftX2 = lineB.end.x - lineA.end.x
            shiftY2 = lineB.end.y - lineA.end.y
            if shiftX1 != shiftX2 or shiftY1 != shiftY2:
                shiftX1 = lineB.start.x - lineA.end.x
                shiftY1 = lineB.start.y - lineA.end.y
                shiftX2 = lineB.end.x - lineA.start.x
                shiftY2 = lineB.end.y - lineA.start.y
            if shiftX1 != shiftX2 or shiftY1 != shiftY2:
                continue
            bestMoveByShift.setdefault((shiftX1, shiftY1), 0)
            bestMoveByShift[(shiftX1, shiftY1)] += 1
    for alignmentCount in bestMoveByShift.values():
        bestMoveCount = min(bestMoveCount, len(linesA) - alignmentCount)

    return bestMoveCount

def getCurrentMoveCount(linesA, bSet, shiftX, shiftY):
    currentMoveCount = len(linesA)
    for line in linesA:
        point1 = Point(line.start.x + shiftX, line.start.y + shiftY)
        point2 = Point(line.end.x + shiftX, line.end.y + shiftY)
        mirrorLine = Line(point1, point2)
        if mirrorLine in bSet:
            currentMoveCount -= 1
        else:
            mirrorLine = Line(point2, point1)
            if mirrorLine in bSet:
                currentMoveCount -= 1

    return currentMoveCount

if __name__ == '__main__':
    main()    