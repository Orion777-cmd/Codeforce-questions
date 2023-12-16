num = int(input())
cupboards = []
for _ in range(num):
    each = list(map(int, input().split()))
    cupboards.append(each)

left = 0
right = 0
for i in range(num):
    left += cupboards[i][0]
    right += cupboards[i][1]

if left > num / 2:
    left = num - left
if right > num / 2:
    right = num - right

print(left + right)