testcases = int(input())
for _ in range(testcases):
    length = int(input())
    array = list(map(int, input().split()))

    array.sort()
    i = 0
    j = length - 1
    res = 0
    while i < j:
        
        res += array[j] - array[i]
        i += 1
        j -= 1
    print(res)






