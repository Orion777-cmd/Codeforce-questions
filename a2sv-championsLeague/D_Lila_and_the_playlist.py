n, p = map(int, input().split())
positivity = list(map(int, input().split()))

prefix_sum = [positivity[0]]
for i in range(1, len(positivity)):
    prefix_sum.append(prefix_sum[-1] + positivity[i])

left = 0
right = 0
res = float('inf')

while right < n:
    if prefix_sum[right] < p:
        right += 1
    else:
        res = min(res, right-left+1)
        min_ = left-1
        while prefix_sum[right] - prefix_sum[left] > p:
            res = min(res, right-left)
            min_ = left
            left += 1
        right += 1
print(min_, res)
