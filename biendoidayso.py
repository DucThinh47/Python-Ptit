while True:
    a = [int(x) for x in input().split()]
    if a == [0,0,0,0]:
        break
    for i in range(0, 100001):
        if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
            print(i)
            break
        tmp = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - tmp)

# 1 3 5 9
# 4 3 2 1
# 0 0 0 0