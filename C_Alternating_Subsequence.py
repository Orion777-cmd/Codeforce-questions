testcases = int(input())
for _ in range(testcases):
    n = int(input())
    arr = list(map(int, input().split()))
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    neg.sort()
    pos.sort(reverse=True)
    i, j = 0, 0
    res = []
    while i < len(neg) and j < len(pos):
        res.append(pos[j])
        res.append(neg[i])
        i += 1 
        j += 1
    if j < len(pos):
        res.append(pos[j])
    elif i < len(neg):
        res.append(neg[i])
    print(sum(res))