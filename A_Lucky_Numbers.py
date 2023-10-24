def lucky_point(x):
    max_digit = 0
    min_digit = 10
    
    while x > 0:
        digit = x % 10
        max_digit = max(max_digit, digit)
        min_digit = min(min_digit, digit)
        x //= 10
        
    return max_digit - min_digit 
test_cases = int(input())
for _ in range(test_cases):
    left, right = map(int, input().split())
    point = lucky_point(left)
    luckiest = left

    right = min(left + 100, right)

    while left <= right:
        temp = lucky_point(left)

        if temp >= point:
            point = temp
            luckiest = left

        left += 1
    
    print(luckiest)
