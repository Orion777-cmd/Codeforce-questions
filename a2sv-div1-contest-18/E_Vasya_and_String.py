length, max_to_change = map(int, input().split())
string = input()

def check(x):
    i = j = cnt = ans = 0
    for i in range(length):
        if string[i] == x:
            cnt += 1
        if cnt > max_to_change:
            while cnt > max_to_change:
                if string[j] == x:
                    cnt -= 1
                j += 1
        ans = max(ans, i - j + 1)
    return ans

print(max(check('b'), check('a')))

