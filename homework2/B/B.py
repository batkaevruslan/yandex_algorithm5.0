def main():
    n, k = list(map(int, input().strip().split()))
    prices = list(map(int, input().strip().split()))

    print(getMaxProfit(prices, k))

def getMaxProfit(prices, k):
    maxProfit = float("-inf")
    n = len(prices)
    for i in range(n):
        startPrice = prices[i]
        currentProfit = float("-inf")
        for j in range(i, min(i + k + 1, n)):
            endPrice = prices[j]
            currentProfit = max(currentProfit, endPrice - startPrice)
        maxProfit = max(maxProfit, currentProfit)
    return maxProfit

if __name__ == '__main__':
    main()    