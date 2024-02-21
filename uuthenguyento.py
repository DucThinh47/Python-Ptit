import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    cnt1 = 0
    cnt2 = 0
    if isPrime(len(s)) == False:
        return "NO"
    else:
        for i in s:
            if isPrime(int(i)) == True:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 < cnt2:
            return "NO"
        return "YES"

t = int(input())
while t > 0:
    s = input()
    print(solve(s))
    t -= 1

# 3
# 1234567
# 22334455667
# 23400300489898989