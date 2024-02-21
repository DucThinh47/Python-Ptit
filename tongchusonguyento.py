import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t >= 1:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum) == True:
        print("YES")
    else:
        print("NO")
    t -= 1

# 2
# 12341
# 22222222222222222222
