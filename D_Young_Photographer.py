sportsmen, position = map(int, input().split())
segments = []
left = float('-inf')
right = float('inf')
for i in range(sportsmen):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    segments.append((a, b))
    left = max(a, left)
    right = min(b, right)
if left > right:
    print(-1)
    exit()
cnt = 0
if position < left:
    cnt = left - position

elif position > right:
    cnt = position - right
print(cnt)
