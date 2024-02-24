import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
a1,a2,flag = [], [], [0] * n
for i in range(n):
    if isPrime(a[i]) == True:
        a1.append(a[i])
    else:
        a2.append(a[i])
        flag[i] = 1
a1 = sorted(a1)
cnt1, cnt2 = 0, 0
for i in range(n):
    if flag[i] == 1:
        print(a2[cnt2], end=" ")
        cnt2 += 1
    else:
        print(a1[cnt1], end=" ")
        cnt1 += 1

# 8
# 4 6 3 8 7 2 5 9