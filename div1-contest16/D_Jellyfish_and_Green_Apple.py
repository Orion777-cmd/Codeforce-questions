testcases = int(input())

for _ in range(testcases):
    greenApple, people = map(int, input().split())

    greenApple %= people

    if greenApple == 0:
        print("0")
        continue

    power_of_2 = 1
    while power_of_2 < people:
        power_of_2 *= 2

    if power_of_2 == people:
        ans = 0
        while greenApple != 0:
            ans += greenApple
            greenApple *= 2
            greenApple %= people

        print(ans)
        continue

    if people % 2 != 0:
        print("-1")
        continue

    temp = people
    while temp % 2 == 0:
        temp //= 2

    if greenApple % temp != 0:
        print("-1")
        continue

    ans = 0
    while greenApple != 0:
        ans += greenApple
        greenApple *= 2
        greenApple %= people
    
    print(ans)