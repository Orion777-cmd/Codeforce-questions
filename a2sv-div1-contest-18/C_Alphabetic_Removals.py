length, letters_to_remove = map(int, input().split())
s = list(input())

start = ord('a')
end = ord('z')

for i in range(start, end + 1):
    for x in range(length):
        if letters_to_remove == 0:
            break
        if s[x] == chr(i):
            s[x] = ' '
            letters_to_remove -= 1
        
result = ''.join(char for char in s if char != ' ')
print(result)