import sys
sys.set_int_max_str_digits(0)

def getTotalIncome(n, k, d):
    currentIncome = n
    for day in range(d + 1):
        possibleIncome = currentIncome * 10
        remainder = possibleIncome % k
        if remainder == 0:
            return currentIncome * pow(10, d - day)
        elif k - remainder > 9:
            return -1
        else:
            currentIncome = possibleIncome + (k - remainder)
    return currentIncome

def main():
    n, k, d = list(map(int, input().strip().split()))
    writer = open('output.txt', 'w')
    writer.write(str(getTotalIncome(n, k, d)))
    writer.write("\n")
    writer.close()

if __name__ == '__main__':
    main()