from collections import deque
from typing import List

def getSignSequence(nums: List[int]):
    result = deque()
    lastIndex = 0
    while lastIndex < len(nums) and (nums[lastIndex] % 2) == 0:
        result.append("+")
        lastIndex += 1
    
    lastIndex += 1
    while lastIndex < len(nums) and (nums[lastIndex] % 2) == 1:
        result.append("x")
        lastIndex += 1
    
    if lastIndex < len(nums):
        result.append("+")
        lastIndex += 1
        while lastIndex < len(nums):
            result.append("x")
            lastIndex += 1

    return "".join(result)

def main():
    n = int(input())
    nums = list(map(int, input().strip().split()))
    print(getSignSequence(nums))

if __name__ == '__main__':
    main()