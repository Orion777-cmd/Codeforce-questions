from collections import Counter
testcases = int(input())

def is_palindrome(array):
    length = len(array)
    for i in range(length//2):
        if array[i] != array[length - i - 1]:
            return False
    return True
for _ in range(testcases):
    length = int(input())
    array = list(map(int, input().split()))
    nums = array.copy()
    dict_ = Counter(array)
    # if length <= 2:
    #     print("YES")
    
    # else:
    for i in range(length):
        x = array[i]
        remaining_length = length - i - 1
        
        if (dict_[x] - 1) * 2 <= remaining_length:
            print( "YES")
            break
    
    print("NO")
