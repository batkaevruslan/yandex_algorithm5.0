
from typing import List

def main():
    berryCount = int(input())
    berries = [None] * berryCount
    for i in range(berryCount):
        berries[i] = list(map(int, input().strip().split()))
    result = getMaxHeight(berries)
    print(result[0])
    print(" ".join(map(str, result[1])))

def getMaxHeight(berries: List[tuple[int, int]]):
    result = []
    maxHeight = 0
   
    maxNonPositiveShiftRaiseIndex = -1
    for i in range(len(berries)):
        currentBerry = berries[i]
        currentShift = currentBerry[0] - currentBerry[1]
        if currentShift > 0:
            if len(result) == 0:
                result.append(i)
            else:
                prevBerryIndex = result[-1]
                prevBerry = berries[prevBerryIndex]
                prevShift = prevBerry[0] - prevBerry[1]
                if prevShift + currentBerry[0] > currentShift + prevBerry[0]:
                    result.append(i)
                else:
                    result[-1] = i
                    result.append(prevBerryIndex)
        else:
            if maxNonPositiveShiftRaiseIndex == -1:
                maxNonPositiveShiftRaiseIndex = i
            else:
                prevNonPositiveShiftRaiseBerry = berries[maxNonPositiveShiftRaiseIndex]
                if currentBerry[0] > prevNonPositiveShiftRaiseBerry[0]:
                    maxNonPositiveShiftRaiseIndex = i
    
    currentHeight = 0
    for i in range(len(result)):
        berryIndex = result[i]
        currentHeight += berries[berryIndex][0]
        maxHeight = currentHeight
        currentHeight -= berries[berryIndex][1]
        result[i] += 1

    if maxNonPositiveShiftRaiseIndex != -1:
        currentHeight += berries[maxNonPositiveShiftRaiseIndex][0]
        maxHeight = max(currentHeight, maxHeight)
        result.append(maxNonPositiveShiftRaiseIndex + 1)

    for i in range(len(berries)):
        currentBerry = berries[i]
        currentShift = currentBerry[0] - currentBerry[1]
        if currentShift <= 0 and i != maxNonPositiveShiftRaiseIndex:
            result.append(i + 1)

    return (maxHeight, result)

if __name__ == '__main__':
    main()   