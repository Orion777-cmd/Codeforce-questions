from collections import defaultdict

test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))
    pairs = 0
    dict_ = defaultdict(int)

    for i in range(length):
        diff = arr[i] - i - 1
        pairs += dict_[diff]
        dict_[diff] += 1

    print(pairs)
