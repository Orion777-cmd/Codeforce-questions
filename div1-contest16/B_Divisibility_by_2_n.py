import math

def get_count(x):
    total = 0
    while x % 2 == 0:
        x //= 2
        total += 1
    return total

testcases = int(input())
for _ in range(testcases):
    leng = int(input())
    arr = list(map(int, input().split()))
    num = 0
    extra = 0
    nums = []
    for i in range(leng):
        num += get_count(arr[i])
        cnt = get_count(i + 1)
        extra += cnt
        nums.append(cnt)
    
    if num >= leng:
        print(0)
        continue
    
    if num + extra < leng:
        print(-1)
        continue
    
    ans = 0
    nums.sort(reverse=True)
    for i in nums:
        ans += 1
        if num + i >= leng:
            break
        num += i
    
    print(ans)
