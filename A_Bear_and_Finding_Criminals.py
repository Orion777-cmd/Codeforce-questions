length, limak = map(int, input().split())
criminals = list(map(int, input().split()))


limak -= 1
dist = 1
total_criminals = 0
while limak -dist > -1 and limak + dist< length:
    
    if criminals[limak -dist] == criminals[limak + dist] == 1:
        total_criminals += 2
    dist += 1

while limak - dist > -1:
    total_criminals += criminals[limak - dist]
    dist += 1

while limak + dist < length:
    total_criminals += criminals[limak + dist]
    dist += 1
    
print(total_criminals + criminals[limak])
    
    


