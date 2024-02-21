def check(s):
    for i in s:
        if i != '4' and i != '7':
            return False
    return True

t = int(input())
while t >= 1:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1