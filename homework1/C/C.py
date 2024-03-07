from collections import deque
from typing import List

def getTotalPressCount(requiredSpaceCountPerLine: List[int]):
    result = 0
    spacesInTab = 4
    for requiredSpaceCount in requiredSpaceCountPerLine:
        tabsCount, remainedSpaces = divmod(requiredSpaceCount, spacesInTab)
        result += tabsCount
        if remainedSpaces == 3:
            result += 2
        else:
            result += remainedSpaces
    return result

def main():
    numberOfLines = int(input())
    requiredSpaceCountPerLine = [0] * numberOfLines
    for i in range(numberOfLines):
        requiredSpaceCountPerLine[i] = int(input())
    print(getTotalPressCount(requiredSpaceCountPerLine))

if __name__ == '__main__':
    main()