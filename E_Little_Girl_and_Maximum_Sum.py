from itertools import accumulate  
num_elements, num_queries = map(int, input().split())
elements = list(map(int, input().split()))

queries = []
for _ in range(num_queries):
    query = list(map(int, input().split()))
    queries.append(query)

elements.sort()
prefix_sum = list(accumulate(elements))
print(prefix_sum)


res = 0
for query in queries:
    start , end = query
    temp_sum = prefix_sum[end - 1] - prefix_sum[start - 1]
    res += temp_sum

print(res)



