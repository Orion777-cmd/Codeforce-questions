testcases = int(input())

for _ in range(testcases):
    length, current = map(str,input().split())
    length = int(length) * 2
    lights = input() * 2

    if current == 'g':
        print(0)
        continue
    max_dist = 0
    cnt = 0
    flag = False

    for i in range(length):
        if lights[i] == 'g':
            max_dist = max(max_dist, cnt)
            flag = False
        if current == lights[i] and flag == False:
            flag = True
            cnt = 0
        if flag:
            cnt += 1

    print(max_dist)
