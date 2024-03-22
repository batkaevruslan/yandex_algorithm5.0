def main():
    a = input().strip()
    b = input().strip()

    print(areAnagram(a, b))

def areAnagram(a, b):
    if len(a) != len(b):
        return "NO"
    
    aCountByChar = {}
    for char in a:
        currentCount = aCountByChar.setdefault(char, 0)
        aCountByChar[char] = currentCount + 1
    
    for char in b:
        currentCount = aCountByChar.setdefault(char, 0)
        if currentCount == 0:
            return "NO"
        aCountByChar[char] = currentCount - 1
    
    return "YES"

if __name__ == '__main__':
    main()    