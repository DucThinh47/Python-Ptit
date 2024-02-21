t = int(input())
while t >= 1:
    n = int(input())
    res = 0.0
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            res += 1.0/i
    else:
        for i in range(1, n+1, 2):
            res += 1.0/i
    print("{:.6f}".format(res))
    t-=1