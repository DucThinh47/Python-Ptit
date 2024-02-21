def check(s):
    fl = False
    for i in s:
        if int(i) % 2 != 0:
            fl = False
        else:
            fl = True
    tmp = int(s[::-1])
    if tmp == int(s) and fl == True and len(s) % 2 == 0:
        return True
    return False

t = int(input())
while t>=1:
    n = int(input())
    for i in range(10, n + 1):
        if(check(str(i))):
            print(i, end=" ")
    print()
    t-=1