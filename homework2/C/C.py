def main():
    input()
    ropes = list(map(int, input().strip().split()))

    print(getMaxProfit(ropes))

def getMaxProfit(ropes):
    maxRope = float("-inf")
    totalLength = 0
    for rope in ropes:
        maxRope = max(maxRope, rope)
        totalLength += rope
    
    if maxRope > totalLength - maxRope:
        return 2 * maxRope - totalLength
    else:
        return totalLength

if __name__ == '__main__':
    main()    