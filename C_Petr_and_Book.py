pages = int(input())
each_day = list(map(int, input().split()))

i = 0
while pages > 0:
    pages -= each_day[i]
    if pages <= 0:
        break
    i = (i + 1) % 7

print(i+1)