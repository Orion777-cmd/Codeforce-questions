test_cases = int(input())

for _ in range(test_cases):
    string = input()
    stack = []
    coin = 0
    for char in string:
       
        while stack and char != 'C':
            letter = stack.pop()
            
            if letter == 'A' and char == 'B':   
                coin += 1
                char = 'B' if stack else 'C'
            elif letter == 'B' and char == 'A':
                coin += 1
                char = 'C' if stack else 'B'
            
            else:
                stack.append(letter)
                break
        
        stack.append(char)
        
    print(coin)

