import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            cnt += 1
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")
    t -= 1