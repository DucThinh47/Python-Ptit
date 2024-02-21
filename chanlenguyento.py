import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def check(s):
    for i in range(0, len(s)):
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return False
        if i % 2 != 0 and int(s[i]) % 2 == 0:
            return False
    return True

t = int(input())
while t>0:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum) == True and check(s) == True:
        print("YES")
    else:
        print("NO")
    t-=1

# 2
# 2345678521
# 1212121212121212121212121