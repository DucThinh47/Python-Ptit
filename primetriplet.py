a = [0] * 1000001

def sang():
    a[0] = a[1] = 1
    for i in range(2, 1001):
        if a[i] == 0:
            for j in range(i*i, 1000001, i):
                a[j] = 1

sang()
t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(0, n):
        if a[i] == 0 and a[i+6] == 0 and (a[i+2] == 0 or a[i+4] == 0) and i+6 < n and (i+2 < n or i+4 < n):
            cnt += 1
    print(cnt)
    t -= 1