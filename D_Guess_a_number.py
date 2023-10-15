queries = int(input())
lower = -2 * 10**9
upper = 2 * 10**9
for _ in range(queries):
    sign, given_num, answer = input().split()
    given_num = int(given_num)
    if sign == '>=':
        if answer == 'Y':
            lower =max(lower, given_num)
        else:
            upper = min(upper, given_num - 1)
    elif sign == '>':
        if answer == 'Y':
            lower = max(lower, given_num + 1)
        else:
            upper = min(upper, given_num)
    elif sign == '<=':
        if answer == 'Y':
            upper = min(upper, given_num)
        else:
            lower = max(lower, given_num + 1)
    else:
        if answer == 'Y':
            upper = min(upper, given_num - 1)
        else:
            lower = max(lower , given_num)
if lower > upper:
    print("Impossible")
else:
    print(lower)
   


    
    

