import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    tmp = s[0:3]
    tmp1 = s[-3::]
    if isPrime(int(tmp)) == True and isPrime(int(tmp1)) == True:
        return "YES"
    return "NO"

t = int(input())
while t>0:
    s = input()
    print(solve(s))
    t-=1

# 3
# 12743
# 7337
# 12345678901234