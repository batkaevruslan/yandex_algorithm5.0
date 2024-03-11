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
    maxRotationCount = minRotationCount % len(prizes) + (maxRotationCount - minRotationCount)  % len(prizes)
    minRotationCount = minRotationCount % len(prizes)
    
    #clockwise
    bestPrize = 0
    for i in range(minRotationCount, maxRotationCount + 1):
        bestPrize = max(bestPrize, prizes[i % len(prizes)])
        anticlockwiseIndex = len(prizes) - i % len(prizes)
        if anticlockwiseIndex < len(prizes):
            bestPrize = max(bestPrize, prizes[anticlockwiseIndex])
    return bestPrize
    # 2 4 6 8
    # 0 1 2 3

if __name__ == '__main__':
    main()    