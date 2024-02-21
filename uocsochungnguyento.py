import math

t = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while t>=1:
    a, b = [int(x) for x in input().split()]
    tmp = math.gcd(a,b)
    sum = 0
    for i in str(tmp):
        sum += int(i)
    if isPrime(sum) == True:
        print("YES")
    else:
        print("NO")
    t-=1