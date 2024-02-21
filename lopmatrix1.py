t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    a = [[0] * m] * n
    b = []
    for i in range(n):
        a[i] = [int(x) for x in input().split()]
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(a[j][i])
        b.append(tmp)
    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(m):
                res += a[i][k] * b[k][j]
            print(res, end = " ")
        print()
# 1
# 2  2
# 1  2
# 3  4