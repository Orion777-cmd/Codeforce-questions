typed = input()
goal = 'hello'
j = 0
ans = 'YES'

for i in range(len(typed)):
    if typed[i] == goal[j]:
        j += 1
    if j == len(goal):
        break
if j < len(goal):
    ans = 'NO'
print(ans)
