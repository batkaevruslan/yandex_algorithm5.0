def main():
    n = int(input())
    prizes = list(map(int, input().strip().split()))
    minAngleSpeed, maxAngleSpeed, speedReduction = list(map(int, input().strip().split()))

    print(getBestprize(prizes, minAngleSpeed, maxAngleSpeed, speedReduction))

def getBestprize(prizes, minAngleSpeed, maxAngleSpeed, speedReduction):
    minRotationCount = minAngleSpeed // speedReduction
    if minAngleSpeed % speedReduction == 0:
        minRotationCount -= 1
    maxRotationCount = maxAngleSpeed // speedReduction
    if maxAngleSpeed % speedReduction == 0:
        maxRotationCount -= 1
    
    if maxRotationCount - minRotationCount >= len(prizes):
        return max(prizes)
    
    minRotationCount = minRotationCount
    maxRotationCount = maxRotationCount
    #clockwise
    bestPrize = 0
    for i in range(minRotationCount % len(prizes), min(len(prizes), maxRotationCount + 1)):
        bestPrize = max(bestPrize, prizes[i])
    
    if maxRotationCount > len(prizes) and maxRotationCount % len(prizes) < minRotationCount % len(prizes):
        for i in range(0, maxRotationCount % len(prizes)):
            bestPrize = max(bestPrize, prizes[i])
    
    #anticlockwise
    leftIndex = len(prizes) - maxRotationCount % len(prizes) if maxRotationCount > 0 else len(prizes)
    rightIndex = len(prizes) - minRotationCount % len(prizes) if minRotationCount > 0 else len(prizes)
    for i in range(leftIndex, rightIndex):
        bestPrize = max(bestPrize, prizes[i])
    return bestPrize
    # 2 4 6 8
    # 0 1 2 3

if __name__ == '__main__':
    main()    