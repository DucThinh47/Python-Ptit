def check(s):
    if len(s) < 4:
        return False
    for i in s:
        if i.isdigit():
            if int(i) < 0 or int(i) > 255:
                return False
        else:
            return False
    return True

t = int(input())
while t > 0:
    s = input().split('.')
    if check(s):
        print("YES")
    else:
        print("NO")
    t -= 1

# 2
# 192.168.1.1
# 256.255.255.255