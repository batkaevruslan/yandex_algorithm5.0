def main():
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    k = int(input())
    requests = [None] * k
    for i in range(k):
        requests[i] = list(map(int, input().strip().split()))
    
    result = getResult(numbers, requests)
    print(" ".join(map(str, result)))

def getResult(numbers, requests):
    numbers.sort()
    results = [0] * len(requests)
    for i in range(len(requests)):
        leftIndex = getGreaterOrEqual(numbers, requests[i][0], 0, len(numbers) - 1)
        rightIndex = getLessOrEqual(numbers, requests[i][1], 0, len(numbers) - 1)

        results[i] = rightIndex - leftIndex + 1
    return results

def getGreaterOrEqual(numbers, number, startIndex, endIndex):
    if startIndex > endIndex:
        return startIndex
    middleIndex = (endIndex + startIndex) // 2
    middleNumber = numbers[middleIndex]
    if middleNumber >= number:
        return getGreaterOrEqual(numbers, number, startIndex, middleIndex - 1)
    else:
        return getGreaterOrEqual(numbers, number, middleIndex + 1, endIndex)
        

def getLessOrEqual(numbers, number, startIndex, endIndex):
    if startIndex > endIndex:
        return endIndex
    middleIndex = (endIndex + startIndex) // 2
    middleNumber = numbers[middleIndex]
    if middleNumber <= number:
        return getLessOrEqual(numbers, number, middleIndex + 1, endIndex)
    else:
        return getLessOrEqual(numbers, number, startIndex, middleIndex - 1)

if __name__ == '__main__':
    main()    