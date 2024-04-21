test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)
    res = 0
    for num in arr_set:
        cnt = arr.count(num)
        if cnt >= 3:
            res += cnt // 3
    print(res)