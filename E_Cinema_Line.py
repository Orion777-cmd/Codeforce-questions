from collections import defaultdict
length = int(input())
money = list(map(int, input().split()))

dict_ = defaultdict(int)
ans = 'YES'
for i in range(length):
    if money[i] == 25:
        dict_[25] += 1
    elif money[i] == 50:
        if dict_[25] > 0:
            dict_[25] -= 1
            dict_[50] += 1
        else:
            ans = 'NO'
            break
    else:
        if dict_[50] > 0 and dict_[25] > 0:
            dict_[50] -= 1
            dict_[25] -= 1
        elif dict_[25] > 2:
            dict_[25] -= 3
        else:
            ans = 'NO'
            break
print(ans)
    
