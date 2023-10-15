numbers = int(input())
for _ in range(numbers):
    num = int(input())
    moves = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            moves += 1
        elif num % 3 == 0:
            num = (2 * num) // 3
            moves += 1
        elif num % 5 == 0:
            num = (4 * num) // 5
            moves += 1
        else:
            moves = -1
            break
    print(moves)