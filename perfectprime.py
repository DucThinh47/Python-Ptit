import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def check(s):
    check1 = True
    for i in range(len(s)):
        if isPrime(int(s[i])) == False:
            check1 = False
    tmp = s[::-1]
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if isPrime(int(s)) == True and isPrime(int(tmp)) == True and isPrime(sum) == True and check1 == True:
        return True
    return False

t = int(input())
while t >= 1:
    s = input()
    if check(s) == True:
        print("Yes")
    else:
        print("No")
    t -= 1