students, x_time, y_time = map(int, input().split())

if students == 1:
    print( min(x_time, y_time))

ans = 0
left = 0
right = max(x_time, y_time) * students

def isPossible(mid, students, x_time, y_time):
    x_copies = mid // x_time
    y_copies = mid // y_time

    return x_copies + y_copies >= students - 1

while left <= right:
    mid = (left + right) // 2

    if isPossible(mid, students, x_time, y_time):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print( ans + min(x_time, y_time) )

