def check(s):
    tmp = s[::-1]
    for i in range(len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(tmp[i]) - ord(tmp[i-1])):
            return False
    return True

t = int(input())
while t>0:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t-=1

# 2
# acxz
# bcxz