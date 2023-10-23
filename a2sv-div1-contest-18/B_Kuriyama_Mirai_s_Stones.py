size = int(input())

monsters = list(map(int, input().split()))
questions = int(input())
sorted = sorted(monsters)
 
cumsum = [0] * (size + 1)
for i in range(1, size + 1):
    cumsum[i] = cumsum[i - 1] + monsters[i - 1]
 
 
sortedCumsum = [0] * (size + 1)
for i in range(1, size + 1):
    sortedCumsum[i] = sortedCumsum[i - 1] + sorted[i - 1]
 
 

for _ in range(questions):
    type, l, r = map(int, input().split())
    tot  = 0
    if(type == 1):
        tot = cumsum[r] -cumsum[l-1]
    else:        
        tot = sortedCumsum[r]- sortedCumsum[l-1]
    print(tot)