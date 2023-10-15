num, minutes_in_battle = map(int, input().split())
strengths = list(map(int, input().split()))
arrows = list(map(int, input().split()))

prefix_sum = [0] * (num + 1)
for i in range(1, num + 1):
    prefix_sum[i] = prefix_sum[i - 1] + strengths[i - 1]
print(prefix_sum)
for i in range(minutes_in_battle):
    arrow = arrows[i]
    left, right = 0, num
    while left < right:
        mid = (left + right + 1) // 2
        
        if prefix_sum[mid] <= arrow:
            left = mid
        else:
            right = mid - 1
    print('left: ', left)
    standing = num - left
    if standing == 0 and arrow >= prefix_sum[1]:
        standing = num
    

    print(standing)