from collections import Counter
bars = int(input())
heights = list(map(int, input().split()))

count = Counter(heights)
height = 0
towers = len(count)

for num, freq in count.items():
    if freq > height:
        height = freq

print(height, towers)

