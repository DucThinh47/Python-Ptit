import math


def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
dic = {}
for i in a:
    dic[i] = 1
a = list(dic)
n = len(a)
# summ = 0
flag = 0
for i in range(1, n):
    a[i] += a[i-1]
for i in range(n):
    if isPrime(a[i]) and isPrime(a[n-1] - a[i]):
        flag = 1
        print(i)
        break;
if flag == 0:
    print("NOT FOUND")

# 10
# 3 6 7 3 4 7 3 6 4 4

# 10
# 3 6 7 3 5 7 3 6 6 7