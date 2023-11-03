test_cases = int(input())   
for _ in range(test_cases):
    length = int(input())
    arrayA = list(map(int, input().split()))
    arrayB = list(map(int, input().split()))
    modulo = 10**9 + 7
    arrayA.sort()
    arrayB.sort()
    res = [0] * length
    ans = 1
    j = 0
    for i in range(length):
        while j < length and arrayA[j] <= arrayB[i]:
            j += 1
        if j != length:
            res[i] = length - j
    
    res.sort()
    for i in range(len(res)):
        ans = (ans * (res[i] - i)) % modulo
    print(ans)
