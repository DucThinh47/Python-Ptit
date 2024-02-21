def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return False
    return True

t = int(input())
while t>=1:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1

# 3
# 1214AB
# 10210221
# 22222222