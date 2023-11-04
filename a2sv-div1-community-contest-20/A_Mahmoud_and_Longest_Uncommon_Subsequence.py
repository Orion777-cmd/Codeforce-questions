stringA = input()
stringB = input()

if stringA == stringB:
    print(-1)
elif len(stringA) != len(stringB):
    print(max(len(stringA), len(stringB)))
else:
    print(len(stringA))