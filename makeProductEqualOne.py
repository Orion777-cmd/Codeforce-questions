length =  int(input())
numbers = list(map(int, input().split()))

coins = 0

posetive = [numbers[i] for i in range(length) if numbers[i] > 0]
negative = [numbers[i] for i in range(length) if numbers[i] < 0]
zeros = length - len(posetive) - len(negative)
negative.sort()

for i in posetive:
   
    coins += i - 1

leng = len(negative)
if leng % 2 == 0:
    for i in negative:
        coins += abs(i + 1)

else:
    for i in range(leng-1):
         coins += abs(negative[i] + 1)
    
    if zeros > 0:

         coins += abs(negative[leng-1] + 1)
    else:
         coins += abs(negative[leng-1]) +1
    
coins += zeros
print(coins)

    
