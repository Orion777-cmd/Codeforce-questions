from collections import Counter

testcases = int(input())
for _ in range(testcases):
    leng, k = map(int, input().split())
    nums = list(map(int, input().split()))

    count_ = Counter(nums)

    k_times = [key for key, val in count_.items() if val == k]

    res = 0
    left, right = -1, -1
    k_times.sort()
    print(k_times)
    max_diff = -1
    for i in range(len(k_times)):
        for j in range(i + 1, len(k_times)):
            if k_times[j] - k_times[i] > max_diff:
                valid_range = True
                for num in range(k_times[i] + 1, k_times[j]):
                    if count_[num] != k:
                        valid_range = False
                        break
                if valid_range:
                    left, right = k_times[i], k_times[j]
                    max_diff = k_times[j] - k_times[i]
    
    if left == -1:
        print(-1)
    else:
        print(left, right)