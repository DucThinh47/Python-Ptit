def idx(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return -1
        if s[i] < s[i-1]:
            return i
    return -1

def check(s):
    if len(s) < 3:
        return False
    tmp = idx(s)
    if tmp == -1:
        return False
    for i in range(tmp + 1, len(s)):
        if s[i] > s[i-1]:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    t -= 1

# 3
# 12342
# 23342
# 5678961