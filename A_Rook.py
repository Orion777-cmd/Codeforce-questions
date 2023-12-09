test_cases = int(input())
for _ in range(test_cases):
    position = input()
    
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    ch = position[0]
    num = position[1]
    for i in range(len(characters)):
        if ch == characters[i]:
            continue
        else:
            print(characters[i]+num)
    for i in range(len(numbers)):
        if num == numbers[i]:
            continue
        else:
            print(ch+numbers[i])
            