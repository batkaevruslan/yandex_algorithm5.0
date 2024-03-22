def main():
    input()
    nums = list(map(int, input().strip().split()))

    print(getMinCountToRemove(nums))

def getMinCountToRemove(nums):
    countByNum = {}
    for n in nums:
        currentCount = countByNum.setdefault(n, 0)
        countByNum[n] = currentCount + 1
    
    minDiff = len(nums)
    for n, count in countByNum.items():
        currentDiff = len(nums) - count
        minDiff = min(currentDiff, minDiff)
        if (n - 1) in countByNum:
            minDiff = min(currentDiff - countByNum[n - 1], minDiff)
        if (n + 1) in countByNum:
            minDiff = min(currentDiff - countByNum[n + 1], minDiff)

    return minDiff

    # 1 2 3
    return 0

if __name__ == '__main__':
    main()    