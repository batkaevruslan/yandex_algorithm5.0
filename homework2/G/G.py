
def main():
    testSetCount = int(input())
    for _ in range(testSetCount):
        n = int(input())
        numbers = list(map(int, input().strip().split()))
        segments = getSegments(numbers)
        print(len(segments))
        print(" ".join(map(str, segments)))
    
def getSegments(numbers):
    segments = []
    left = 0
    right = 0
    segmentMin = numbers[0]
    while right < len(numbers):
        right += 1
        if right == len(numbers):
            segments.append(right - left)
        elif right - left >= segmentMin or right - left >= numbers[right]:
            segments.append(right - left)
            left = right
            segmentMin = numbers[right]
        else:
            segmentMin = min(segmentMin, numbers[right])
    return segments
    # 1 3 3 3 2
if __name__ == '__main__':
    main()   