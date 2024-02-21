import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = [int(x) for x in input().split()]

for i in range(n):
    a = [int(x) for x in input().split()]
    for j in a:
        if isPrime(j) == True:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9