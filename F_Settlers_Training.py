from collections import Counter
soldiers, ranks = map(int, input().split())
soldiers_list = list(map(int, input().split()))

count = [0] * (ranks)

for i in soldiers_list:
    count[i - 1] += 1

golds = 0

while count[ranks - 1] != soldiers:
    temp = []
    for i in range(ranks - 1):
        if count[i] > 0:
            temp.append(i)
    
    for i in temp:
        count[i] -= 1
        count[i + 1] += 1
    golds += 1
print(golds)