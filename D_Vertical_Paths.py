
testcases = int(input())
for _ in range(testcases):

    length = int(input())
    parent = [0] * (length + 1)
    vis = [0] * (length + 1)
    deg = [0] * (length + 1)
    input_list = list(map(int, input().split()))
    for i in range(1, length + 1):
        parent[i] = input_list[i - 1]
        deg[i] += 1
        deg[parent[i]] += 1
    leaf = []
    for i in range(1, length + 1):
        if deg[i] == 1:
            leaf.append(i)
    if length == 1:
        print(1)
        print(1)
        print(1)
        continue
    print(len(leaf))
    for i in leaf:
        path = []
        j = i
        while vis[j] == 0:
            path.append(j)
            vis[j] = 1
            j = parent[j]
        print(len(path))
        path.reverse()
        for x in path:
            print(x, end=" ")
        print()
    

