t = int(input())
while t > 0:
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    cnt = 0
    for i in range(0, n-2):
        tmp = a[i]
        l = i + 1
        r = len(a) - 1
        while l < r:
            if tmp + a[l] + a[r] == 0:
                cnt += 1
                l += 1
            elif tmp + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    print(cnt)
    t -= 1

# 2
# 5
# 0 -1 2 -3 1
# 5
# 1 -2  1  0  5