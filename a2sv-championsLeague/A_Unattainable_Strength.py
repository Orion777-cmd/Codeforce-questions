no_of_artefacts = int(input())
artefacts = list(map(int, input().split()))

artefacts.sort()

smallest = 1

for i in range(no_of_artefacts):

    if artefacts[i] > smallest:
        break
    smallest += artefacts[i]

print(smallest)