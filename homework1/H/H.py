
def getMinimumTime(l, x1, v1, x2, v2):
    if v2 < 0 and v1 < 0:
        x2 = l - x2
        x1 = l - x1
        v1 *= -1
        v2 *= -1
    if x2 < x1:
        x2, x1 = x1, x2
        v2, v1 = v1, v2
    if x1 < x2 and v1 > v2 or v1 * v2 < 0:
        return ("yes", abs((x2 - x1) / (v1 - v2)))
    elif v1 == 0 and v2 == 0:
        if x1 == x2:
            return ("yes", 0)
        else:
            return ("no", -1)
    else:
        t1 = (l - x2 - x1) / (v1 + v2)
        if t1 < 0:
            t1 = (l + l - x2 - x1) / (v1 + v2)
        return ("yes", t1)
"""def getMinimumTime(l, x1, v1, x2, v2):
    if v1 < 0 and v2 < 0:
        x1 = l - x1
        x2 = l - x2
        v1 = -v1
        v2 = -v2
    if v1 == 0 and v2 == 0:
        if x1 == x2:
            return ("yes", 0)
        else:
            return ("no", -1)
    t1 = (l - x2 - x1) / (v1 + v2)
    if v1 == v2:
        return ("yes", t1)
    else:
        t2 = (x1 - x2) / (v2 - v1)
        if t1 < 0:
            return ("yes", t2)
        elif t2 < 0:
            return ("yes", t1)
        else:
            return ("yes", min(t1, t2))"""
    
def main():
    l, x1, v1, x2, v2 = list(map(int, input().strip().split()))
    answer, time = getMinimumTime(l, x1, v1, x2, v2)
    print(answer)
    if answer == "yes":
        print(time)

if __name__ == '__main__':
    main()