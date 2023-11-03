num_length, query_length = map(int, input().split())
nums = list(map(int, input().split()))
query = list(map(int, input().split()))

nums.sort()

for num in query:
    ans = "NO"
    lo = 0
    hi = num_length - 1 
    while lo <= hi:
        mid = (hi + lo)//2
        if nums[mid] == num:
            ans = "YES"
            break
        elif nums[mid] < num:
            lo = mid + 1
        else:
            hi = mid -1
    print(ans)