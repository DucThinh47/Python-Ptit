import math

t = int(input())
while t >= 1:
    n,x,m = [float(x) for x in input().split()]
    x /= 100
    y = math.log(m/n, 1 + x)
    if y != int(y):
        y += 1
    print(int(y))
    t -= 1
# 2
# 200.00 6.5 300
# 500 4 1000.00