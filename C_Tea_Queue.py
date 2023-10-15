from collections import deque   
testcases = int(input())
for _ in range(testcases):
    sub = int(input())
    array = []
    for _ in range(sub):
        subarray = list(map(int, input().split()))
        array.append(subarray)
    queue = deque()
    result = [0] * sub
    for i in range(sub):
        arrive, leave = array[i]
        while queue and queue[0][0] < arrive:
            _, end = queue.popleft()
            if queue and end < leave:
                result[queue[0][1]] = end
        if not queue:
            result[i] = arrive
        else:
            result[i] = max(queue[-1][1], arrive)
        queue.append((arrive, result[i] + 1))

    print(*result)


