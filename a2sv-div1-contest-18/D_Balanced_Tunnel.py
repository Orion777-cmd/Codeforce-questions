length = int(input())
entered = list(map(int, input().split()))
exited = list(map(int, input().split()))

diction = {}


fined = 0
for i in range(length-1, -1, -1):
    
    while diction.get(exited[-1], 0) != 0 and len(exited) > 0:
        
        exited.pop()
   
    if exited[-1] != entered[i]:
        fined += 1
    diction[entered[i]] = 1

print(fined)

