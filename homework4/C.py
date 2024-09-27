import bisect


def main():
    n, m = list(map(int, input().strip().split()))
    troops = list(map(int, input().strip().split()))
    requests = [None] * m
    for i in range(m):
        requests[i] = list(map(int, input().strip().split()))
    
    results = getResults(troops, requests)
    for result in results:
        print(result)

def getResults(troops, requests):
    results = [-1] * len(requests)
    cumulativeSum = [troops[0]] * len(troops)
    for i in range(1, len(cumulativeSum)):
        cumulativeSum[i] = troops[i] + cumulativeSum[i - 1]
    
    for i, request in enumerate(requests):
        troopsTotalCount = request[1]
        leftIndex = -1
        leftSum = 0
        rightIndex = getRightIndex(troops, troopsTotalCount)
        currentSum = cumulativeSum[rightIndex]
        while rightIndex > request[0] + leftIndex:
            if cumulativeSum[request[0] + leftIndex] >= troopsTotalCount:
                rightIndex -= 1
            elif currentSum - troops[leftIndex + 1] >= troopsTotalCount:
                leftIndex += 1
                leftSum = cumulativeSum[leftIndex]
            else:
                break
            currentSum = cumulativeSum[rightIndex] - leftSum
        
        if currentSum == troopsTotalCount and rightIndex - leftIndex == request[0]:
            results[i] = leftIndex + 2
    
    return results

def getRightIndex(troops, troopsTotalCount):
    return bisect.bisect_left(troops, troopsTotalCount)

if __name__ == '__main__':
    main()   