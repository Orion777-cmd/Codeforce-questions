num = int(input())
stones = input()

i = 0
count = 0

while i < num - 1:
    if stones[i] == stones[i + 1]:
        count += 1
    i += 1

print(count)