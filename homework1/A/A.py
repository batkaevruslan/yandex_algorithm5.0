def read_inputs() -> tuple[int, int]:
    a, b = list(map(int, input().strip().split()))
    return a, b


def getTotalTreeCount(p: int, v: int, q: int, m: int):
    left1 = p - v
    right1 = p + v
    left2 = q - m
    right2 = q + m
    doIntersect = (left1 >= left2 or right1 >= left2) and (left1 <= right2 or right1 <= right2)
    #print(doIntersect)
    if doIntersect:
        left = min(p - v, q - m)
        right = max(p + v, q + m)
        return getTreeCount(left, right)
    else:
        return getTreeCount(left1, right1) + getTreeCount(left2, right2)

def getTreeCount(left: int, right: int):
    #print(f"l: {left} r:{right}")
    return right - left + 1
#  1 3
def main():
    p, v = read_inputs()
    q, m = read_inputs()
    print(getTotalTreeCount(p, v, q, m))
    #print(getTotalTreeCount(0, 7, 12, 5))

#1 2 3 4 5 6 7 8 9 10 11 12

if __name__ == '__main__':
    main()