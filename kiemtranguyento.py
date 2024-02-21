import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t >= 1:
    s = input()
    tmp = int(s[-4::])
    if isPrime(tmp):
        print("YES")
    else:
        print("NO")
    t-=1

# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999
