import math

n,k = [int(x) for x in input().split()]
cnt = 1
l = 10**(k-1)
r = 10**k
for i in range(l,r):
    if math.gcd(i,n) == 1:
        print(i, end=" ")
        if cnt % 10 == 0:
            print()
        cnt += 1