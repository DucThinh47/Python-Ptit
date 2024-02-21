t = int(input())
while t >= 1:
    s = input()
    tmp = s[0] + s[1]
    tmp1 = s[len(s) - 2] + s[len(s) - 1]
    if int(tmp) == int(tmp1):
        print("YES")
    else:
        print("NO")
    t -= 1
# 3
# 12321
# 1234512
# 10233211111
