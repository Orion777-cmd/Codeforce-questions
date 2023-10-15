import math

def sum_of_path(n):
    depth = int(math.log2(n)) + 1
    lca_sum = (2**depth - 1) // 3
    if n == 2**depth - 1:
        path_sum = (n - 2**(depth - 1) + 1) * (depth - 1)
    else:
        d = depth - 1
        path_sum = (n - 2**(depth - 1) + 2**(depth - d) - 1) * d
    return lca_sum + path_sum

testcases = int(input())
for _ in range(testcases):
    n = int(input())
    print(sum_of_path(n))