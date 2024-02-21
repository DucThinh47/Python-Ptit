def check(n, a, b):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    if check(n, a, b):
        print("YES")
    else:
        print("NO")
    t -= 1
# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84