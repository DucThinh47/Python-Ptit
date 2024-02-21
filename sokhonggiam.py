def check(s):
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False
    return True

t = int(input())
while t >= 1:
    n = input()
    if check(n) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
# 2
# 12345678888888888888889
# 65645645465754765876857685846
