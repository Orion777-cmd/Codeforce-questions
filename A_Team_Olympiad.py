length = int(input())
students = list(map(int, input().split()))

programming = []
math = []
pe = []
answer = []
for i in range(length):
    if students[i] == 1:
        programming.append(i+1)
    elif students[i] == 2:
        math.append(i+1)
    else:
        pe.append(i+1)

i , j , k = 0 , 0, 0
while i < len(programming) and j  < len(math) and k < len(pe):
    answer.append([programming[i], math[j], pe[k]])
    i += 1
    j += 1
    k += 1
print(len(answer))
for ans in answer:
    print(*ans)
