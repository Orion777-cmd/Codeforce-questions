import bisect 

test_cases = int(input())

for _ in range(test_cases):
    num, left, right = map(int, input().split())
    arr = list(map(int, input().split()))
   
    arr.sort()
    res = 0
    
    def binary_search(num, l, r):
        while l < r:
            mid = (l + r) // 2
            if num + arr[mid] > right: 
                r = mid
            else:
                l = mid + 1
        return l
    
    for i in range(num):
        upper_bound = binary_search(arr[i], i + 1, num)
        lower_bound = bisect.bisect_left(arr, left - arr[i], i + 1, upper_bound)  
        res += upper_bound - lower_bound
    
    print(res)