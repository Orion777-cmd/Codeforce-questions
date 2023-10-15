testcases = int(input())
for testcase in range(testcases):
    string = input()
    res = 0
    length = len(string)
    prev_index = -1
    for i in range(length):
        if string[i] == 'R':
            
            res = max(res, i - prev_index)
            prev_index = i
    res = max(res, length - prev_index)
    
    print(res)