from collections import deque

card_length, query_length = map(int, input().split())
card_colors = list(map(int, input().split()))
queries = list(map(int, input().split()))

color_indices = {}
for i in range(card_length):
    if card_colors[i] not in color_indices:
        color_indices[card_colors[i]] = i

for i in range(query_length):
    query = queries[i]
    print(color_indices[query] + 1, end=" ")
    for color in color_indices:
        if color_indices[color] < color_indices[query]:
            color_indices[color] += 1
    color_indices[query] = 0

print()

