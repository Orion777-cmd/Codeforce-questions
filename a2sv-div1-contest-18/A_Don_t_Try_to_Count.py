test_cases = int(input())
for _ in range(test_cases):
    x_leng, s_leng = map(int, input().split())
    x = input()
    s = input()
  
    def check_s_in_x(x, s):
        for i in range(x_leng - s_leng + 1):
            if x[i:i + s_leng] == s:
                return True
        return False

    op = 0
   
    found = False
    while x_leng <= 100 :
        x = x + x
        
        if check_s_in_x(x, s):
            found = True
            break
        op += 1
        x_leng *= 2
    print(op if found else -1)

