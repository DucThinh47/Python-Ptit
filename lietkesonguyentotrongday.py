import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m = {}
n = int(input())
a = [int(x) for x in input().split()]
for i in a:
    if isPrime(i) == True:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
for i in m:
    print(i, m[i])

# 10
# 2 4 7 5 7 8 9 3 7 2