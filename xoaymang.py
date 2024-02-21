t = int(input())
while t > 0:
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(k,n):
        print(a[i], end = " ")
    for i in range(0,k):
        print(a[i], end = " ")
    print()
    t -= 1

# 2
# 5 2
# 1 2 3 4 5
# 10 3
# 2 4 6 8 10 12 14 16 18 20