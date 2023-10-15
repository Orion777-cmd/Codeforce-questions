test_case = int(input())
 
for _ in range(test_case):
    n = int(input())
    string = input()
    count = 0
 
    for i in range(n - 2):
        if string[i] == string[i + 2]:
            count += 1
                    
    print(n - 1 - count)