num = int(input())
numbers = list(map(int, input().split()))


one = numbers.count(1)
sum_val = 0
ans = 0

for i in range(num):
    if numbers[i] == 0:
        sum_val += 1
    else:
        sum_val -= 1
    ans = max(ans, sum_val)
    if sum_val < 0:
        sum_val = 0

if one == num:
    print(num - 1)
else:
    print(one + ans)