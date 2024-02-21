import math

t = int(input())

while t > 0:
    a = input()
    b = a[::-1]
    tmp = math.gcd(int(a), int(b))
    if tmp == 1:
        print("YES")
    else:
        print("NO")
    t -= 1

# 2
# 123
# 997