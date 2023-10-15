testcases = int(input())
for _ in range(testcases):
    leng = int(input())
    string = input()
    sum = 0
    current = [0] * leng
    change = [0] * leng

    for i in range(leng):
        if string[i] == 'L':
            current[i] = max(0, i)
        else:
            current[i] = max(0, leng - i - 1)
        change[i] = leng - 1 - current[i]
        change[i] = change[i] - current[i]
        sum += current[i]
    res = []
    change.sort(reverse=True)
    for k in range(1, leng + 1):
        if change[k - 1] > 0:
            sum += change[k - 1]
        res.append(sum)
    print(*res)
        