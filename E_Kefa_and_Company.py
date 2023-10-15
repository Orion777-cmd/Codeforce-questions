length, min_diff = map(int, input().split())

friends = []
for i in range(length):
    money, factor = map(int, input().split())
    friends.append((money, factor))
friends.sort()

max_sum = 0
company = []
left = 0
right = 0
sum_s = 0
while right < length:
   
    sum_s += friends[right][1]
    company.append(friends[right])

    while left < right and friends[right][0] - friends[left][0] >= min_diff:
        sum_s -= friends[left][1]
        company.remove(friends[left])
        left += 1

    if sum_s > max_sum:
        max_sum = sum_s

    right += 1

print(max_sum)