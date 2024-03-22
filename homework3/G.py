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
    
def main():
    n = int(input())
    points = []
    for _ in range(n):
        pointX, pointY = list(map(int, input().strip().split()))
        points.append(Point(pointX, pointY))

    missingPoints = findMissingPoints(points)
    print(len(missingPoints))
    for point in missingPoints:
        print(f"{point.x} {point.y}") 

def findMissingPoints(points:List[Point]):    
    if len(points) == 1:
        missingPoint = Point(points[0].x + 1, points[0].y + 1)
        points.append(missingPoint)
        missingPoints = findMissingPoints(points)
        return missingPoints + [missingPoint]

    pointSet = set(points)
    missingPoints = None
    for i, point1 in enumerate(points):
        for j in range(i + 1, len(points)):
            point2 = points[j]
            middleX = (point1.x + point2.x) / 2
            middleY = (point1.y + point2.y) / 2
            deltaX = abs(point1.x - point2.x) / 2
            deltaY = abs(point1.y - point2.y) / 2
            point3 = getPoint(point1, point2, middleX + deltaY, middleY, deltaX)
            point4 = getPoint(point1, point2, middleX - deltaY, middleY, -deltaX)
            currentMissingPoints = []
            if point3 != None and point4 != None:
                if point3 not in pointSet:
                    currentMissingPoints.append(point3)
                if point4 not in pointSet:
                    currentMissingPoints.append(point4)
                if missingPoints == None or len(currentMissingPoints) < len(missingPoints):
                    missingPoints = currentMissingPoints
    return missingPoints

def getPoint(point1, point2, x3, middleY, deltaX):
    y3 = middleY + deltaX
    point3 = None
    if (x3 == int(x3) and y3 == int(y3) 
        and (pow(point1.x - x3, 2) + pow(point1.y - y3, 2)) == pow(point2.x - x3, 2) + pow(point2.y - y3, 2)):
        point3 = Point(int(x3), int(y3))
    if point3 != None and point3 != point1 and point3 != point2:
        return point3
    
    y3 = middleY - deltaX
    if (x3 == int(x3) and y3 == int(y3)
        and (pow(point1.x - x3, 2) + pow(point1.y - y3, 2)) == pow(point2.x - x3, 2) + pow(point2.y - y3, 2)):
        point3 = Point(int(x3), int(y3))
    if point3 != None and point3 != point1 and point3 != point2:
        return point3

if __name__ == '__main__':
    main()    