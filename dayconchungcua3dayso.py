t = int(input())
for i in range(t):
    n,m,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d1,d2,d3 = 0,0,0
    flag = 0
    while d1 < n and d2 < m and d3 < k:
        if a[d1] == b[d2] == c[d3]:
            print(a[d1], end = " ")
            flag = 1
            d1 += 1
            d2 += 1
            d3 += 1
        elif a[d1] < b[d2]:
            d1 += 1
        elif b[d2] < c[d3]:
            d2 += 1
        elif c[d3] < a[d1]:
            d3 += 1
    if flag == 0:
        print("NO")
    else:
        print()

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9