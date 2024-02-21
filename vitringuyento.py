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
        if isPrime(i) == True and isPrime(int(s[i])) == False:
            return False
        if isPrime(i) == False and isPrime(int(s[i])) == True:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1

# 2
# 14239567
# 2314514535353