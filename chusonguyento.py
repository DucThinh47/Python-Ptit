import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if isPrime(int(i)):
            cnt1 += 1
        else:
            cnt2 += 1
    if isPrime(len(s)) == True and cnt1 > cnt2:
        return True
    return False

t = int(input())
while t >= 1:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1

# 3
# 1234567
# 22334455667
# 23400300489898989