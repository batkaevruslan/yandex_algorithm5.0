def main():
    n, k = list(map(int, input().strip().split()))
    nums = list(map(int, input().strip().split()))

    print(isAnyRepetitions(nums, k))

def isAnyRepetitions(nums, k):
    countByNum = {}
    for i in range(len(nums)):
        currentNum = nums[i]
        currentCount = countByNum.setdefault(currentNum, 0)
        if currentCount > 0:
            return "YES"
        
        countByNum[currentNum] = 1
        
        if i - k >= 0:
            numToRemove = nums[i - k]
            countByNum[numToRemove] -= 1

    return "NO"

if __name__ == '__main__':
    main()    