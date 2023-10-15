entrances = int(input())

queue = list(map(int, input().split()))

allen = 0
minutes = 0
ceil = max(queue)
while minutes <= ceil and  queue[allen] - minutes > 0:
    
    allen = (allen +1) % entrances
    minutes += 1

print(allen+1)
    

