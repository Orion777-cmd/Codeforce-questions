from collections import defaultdict
guests, guards = map(int, input().split())
entrances = input()
temp = 0
dict_ = defaultdict(int)
dict_2 = defaultdict(int)

for i in range(guests):
    dict_[entrances[i]] += 1
    dict_2[entrances[i]] = 1

for i in range(guests):
    dict_[entrances[i]] -= 1
    
    if dict_2[entrances[i]] == 1:
        temp += 1
    
    if temp > guards:
        print("YES")
        exit()
    
    if dict_[entrances[i]] == 0:
        temp -= 1
    dict_2[entrances[i]] = 0

print("NO")