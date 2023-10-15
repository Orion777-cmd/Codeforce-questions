testcases = int(input())
for _ in range(testcases):
    length = int(input())
    candies = list(map(int, input().split()))

    prefix_sum = [0] * length
    prefix_sum[0] = candies[0]
    for i in range(1, length):
        prefix_sum[i] = prefix_sum[i - 1] + candies[i]
 
    alice = 0
    bob = 0
    total_candies = 0
    
    for i in range(length - 1, -1, -1):
        bob += candies[i]
        l, r = 0, i - 1
        index = -1
        while l <= r:
            mid = l + (r - l) // 2

            if prefix_sum[mid] == bob:
                index = mid
                leftPart = index + 1
                rightPart = length - i
                total_candies = max(total_candies, leftPart + rightPart)
                l = mid + 1
            elif prefix_sum[mid] > bob:
                r = mid - 1
            else:
                l = mid + 1
    
                
    print(total_candies)
        