
n, m = map(int, input().split())
arr = list(map(int, input().split()))

distinct = [0]* (n+1)
seen = set()

for i in range(n-1, -1, -1):
    seen.add(arr[i])
    distinct[i] = len(seen)

for _ in range(m):
    print(distinct[int(input())-1])
