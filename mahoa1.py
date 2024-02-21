t = int(input())

def solve(s):
    cnt = 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            print(cnt, end="")
            print(s[i-1], end="")
            cnt = 1
        else:
            cnt += 1
    print(cnt, end="")
    print(s[len(s)-1])

while t>=1:
    s = input()
    solve(s)
    t -= 1

# 3
# AACDDPQ
# 11111147g
# 1111111111