test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))
    min_ = 1
    max_ = length
    l, r = 0, length - 1
    count = 0
    flag = 0

    while l < r:
        if arr[l] == min_:
            l += 1
            min_ += 1
            count += 1

        if arr[r] == min_:
            r -= 1
            min_ += 1
            count += 1

        if arr[l] == max_:
            l += 1
            max_ -= 1
            count += 1

        if arr[r] == max_:
            r -= 1
            max_ -= 1
            count += 1

        if count == 0:
            print(l + 1, r + 1)
            flag += 1
            break

        count = 0

    if flag == 0:
        print(-1)