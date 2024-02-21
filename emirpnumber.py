a = [0] * 1000001

def sang():
    a[0] = a[1] = 1
    for i in range(2, 1001):
        if a[i] == 0:
            for j in range(i * i, 1000001, i):
                a[j] = 1

sang()
t = int(input())
while t > 0:
    n = int(input())
    for i in range(1, n):
        tmp = int(str(i)[::-1])
        if tmp < n and tmp > i and a[i] == 0 and a[tmp] == 0:
            print(i, tmp, end = " ")
    print()
    t -= 1