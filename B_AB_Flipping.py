test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    string = input()

    stack = []
    op = 0
   
    for i in range(length):
        
        if stack and string[i] == 'B':
            num = stack[-1]
            while stack and string[stack[-1]] == 'A':       
                stack.pop()
                op += 1
            stack.append(num)
        else:
            stack.append(i)
    print(op)
