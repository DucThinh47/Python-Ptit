import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = [int(x) for x in input().split()]
a = [[]] * n
tmp = 0
for i in range(n):
    a[i] = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]) and a[i][j] > tmp:
            tmp = a[i][j]
if tmp == 0:
    print("NOT FOUND")
else:
    print(tmp)
for i in range(n):
    for j in range(m):
        if a[i][j] == tmp:
            print("Vi tri [", i , "][" , j , "]", sep = "")

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
