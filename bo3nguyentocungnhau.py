import math

def check(a,b):
    if math.gcd(a,b) == 1:
        return True
    return False

a,b = [int(x) for x in input().split()]
for i in range(a, b + 1):
    for j in range(i + 1, b + 1):
        for k in range(j + 1, b + 1):
            if check(i,j) and check(i,k) and check(j, k):
                print("(", end="")
                print(i, end=", ")
                print(j, end=", ")
                print(k, end=")\n")
