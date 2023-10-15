
testcases = int(input())
for testcase in range(testcases):
    length, min_days, max_temp = map(int, input().split())
    temperatures = list(map(int, input().split()))
    count = 0
    i = 0

    while i < length:
        if temperatures[i] > max_temp:
            i += 1
            continue

        temp_count = 0
        while i < length and temperatures[i] <= max_temp:
            i += 1
            temp_count += 1

        if temp_count >= min_days:
            tot = (temp_count - min_days) + 1
            count += (tot + 1) * tot // 2
    print(count)

