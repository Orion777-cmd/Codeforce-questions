testcases = int(input())

for _ in range(testcases):
    hole, length = map(int, input().split())
    mouses = list(map(int, input().split()))

    cat = 0
    mouses_survived = 0

    mouses.sort(reverse=True)
    i = 0
    while i < len(mouses) and cat < hole:
        
        if mouses[i] <= cat:
            i += 1
            continue
        else:
            mouses_survived += 1
            cat += hole - mouses[i]
            i += 1
    print(mouses_survived)
