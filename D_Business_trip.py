k = int(input())
months = list(map(int, input().split()))

months.sort(reverse=True)
i = 0
while k >0:
    k -= months[i]
    if k > 0 and len(months) == i + 1:
        i = -1
        break
   
    i += 1
print(i)
