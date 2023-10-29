test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    prices = list(map(int, input().split()))
    max_price = prices[num-1]
    res = 0
    
    for i in range(num-2, -1, -1):
        if prices[i] > max_price:
            res += 1
        max_price = min(max_price, prices[i])
    print(res)