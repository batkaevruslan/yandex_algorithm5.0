def main():
    input()
    list1 = list(map(int, input().strip().split()))
    input()
    list2 = list(map(int, input().strip().split()))
    input()
    list3 = list(map(int, input().strip().split()))

    duplicates = getDuplicates(list1, list2, list3)
    print(" ".join(map(str, duplicates)))

def getDuplicates(list1, list2, list3):
    uniqueNumsList1 = set(list1)
    uniqueNumsList2 = set(list2)
    uniqueNumsList3 = set(list3)
    result = set()
    
    for n in uniqueNumsList1:
        if n in uniqueNumsList3 or n in uniqueNumsList2:
            result.add(n)

    for n in uniqueNumsList2:
        if n in uniqueNumsList3:
            result.add(n)
    
    return sorted(result)


if __name__ == '__main__':
    main()    