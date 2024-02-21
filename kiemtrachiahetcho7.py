t = int(input())
while t > 0:
    n = int(input())
    while n % 7 != 0:
        n += int(str(n)[::-1])
    print(n)
    t -= 1

# 5
# 1
# 2
# 3
# 4
# 999999