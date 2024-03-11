
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
    maxPositiveShift = 0
    maxPositiveShiftBerry = None
    maxPositiveShiftBerryIndex = -1

    maxNonPositiveShiftBerryIndex = -1
    maxNonPositiveShiftBerry = (-1, -1)
    for i in range(len(berries)):
        currentBerry = berries[i]
        currentShift = currentBerry[0] - currentBerry[1]
        if currentShift > 0:
            if currentShift > maxPositiveShift:
                if maxPositiveShiftBerryIndex != -1:
                    result.append(maxPositiveShiftBerryIndex + 1)
                    maxHeight += maxPositiveShift
                maxPositiveShiftBerryIndex = i
                maxPositiveShift = currentShift
                maxPositiveShiftBerry = currentBerry
            else:
                result.append(i)
                maxHeight += currentShift
        elif currentBerry[0] > maxNonPositiveShiftBerry[0]:
            maxNonPositiveShiftBerryIndex = i
            maxNonPositiveShiftBerry = currentBerry
    
    if maxPositiveShift + maxNonPositiveShiftBerry[0] > maxPositiveShiftBerry[0]:
        maxHeight += maxPositiveShift + maxNonPositiveShiftBerry[0]
        result.append(maxPositiveShiftBerryIndex + 1)
        result.append(maxNonPositiveShiftBerryIndex + 1)
    else:
        maxHeight += maxNonPositiveShiftBerry[0]
        result.append(maxNonPositiveShiftBerryIndex + 1)
        result.append(maxPositiveShiftBerryIndex + 1)

    for i in range(len(berries)):
        currentBerry = berries[i]
        currentShift = currentBerry[0] - currentBerry[1]
        if currentShift <= 0 and i != maxNonPositiveShiftBerryIndex:
            result.append(i + 1)
    
    return (maxHeight, result)

if __name__ == '__main__':
    main()   