f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for i in range(t):
    n, b = [int(x) for x in input().split()]
    res = ""
    while (n > 0):
        tmp = n % b
        res = f[tmp] + res
        n = int(n / b)
    print(res)

# 3
# 10 2
# 2021 2
# 31 16