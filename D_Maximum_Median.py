n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
def check(mid, k, sliced):
    operations = 0
    for num in sliced:
        if num < mid:
            operations += mid - num
            
    return operations <= k
 
arr.sort()
left = arr[n//2]
right = left + k + 1
 
while right - left > 1:
    mid = (right + left) // 2
    if check(mid, k, arr[n // 2:]):
        left = mid
        
    else:
        right = mid
 
print(left)