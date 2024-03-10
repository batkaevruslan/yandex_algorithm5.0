def main():
    n = int(input())
    points = []
    for _ in range(n):
        point = list(map(int, input().strip().split()))
        points.append(point)

    minX, minY, maxX, maxY = getRectanglePoints(points)
    print(f"{minX} {minY} {maxX} {maxY}")

def getRectanglePoints(points):
    minX = float("inf")
    minY = float("inf")
    maxX = float("-inf")
    maxY = float("-inf")
    for point in points:
        minX = min(minX, point[0])
        minY = min(minY, point[1])
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])
    return (minX, minY, maxX, maxY)

if __name__ == '__main__':
    main()    