t = int(input())
for i in range(t):
    n,m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b , c = [] , []
    maxx = max(a)
    for i in range(n):
        if a[i] == maxx:
            a.insert(i, m)
            break
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)
    for i in b:
        print(i, end = " ")
    for i in c:
        print(i, end = " ")
    print()

# 1
# 5 3
# -1 2 3 4 -1