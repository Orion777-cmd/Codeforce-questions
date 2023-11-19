num = input()
answer = input()

num_list = [int(i) for i in num]

num_list.sort()

if num_list[0] == 0:
    for i in range(1, len(num_list)):
        if num_list[i] != '0':
            num_list[0], num_list[i] = num_list[i], num_list[0]
            break

ans = ''.join(map(str, num_list))

if answer == ans:
    print("OK")
else:
    print("WRONG_ANSWER")