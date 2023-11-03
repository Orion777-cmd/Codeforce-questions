num_length, query_length = map(int, input().split())
nums = list(map(int, input().split()))
query = list(map(int, input().split()))

for num in query:
    lo, hi = 0 , num_length-1
    ans = 0
    while lo <= hi:
        mid = (hi + lo) //2
        if nums[mid] > num:
            hi = mid - 1
        elif nums[mid] < num:
            lo = mid + 1
        else:
            ans = mid
            break
    print(ans)
