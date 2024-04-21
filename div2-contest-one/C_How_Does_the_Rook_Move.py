modulo = 10 ** 9 +7
test_cases = int(input())
for _ in range(test_cases):
    size, made_moves = map(int, input().split())
    moves = []
    for _ in range(made_moves):
        x, y = map(int, input().split())
        moves.append([x, y])
    