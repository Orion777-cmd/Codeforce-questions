from collections import Counter


test_case = int(input())
for _ in range(test_case):
    length = int(input())
    nums = list(map(int, input().split()))

    dict_ = {}
    
    for i in range(1, length):
        
        if nums[i] != nums[i - 1]:
            dict_[i] = nums[i - 1] - nums[i]
            
    dict_[length] = nums[-1]
    count_ = Counter(nums)
    if dict_ == count_:
        print("YES")
    else:
        print("NO")