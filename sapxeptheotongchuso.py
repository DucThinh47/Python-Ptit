import functools


def tong(n):
    summ = 0
    while n > 0:
        summ += int(n % 10)
        n = int(n / 10)
    return summ

def cmp(a, b):
    if tong(a) == tong(b):
        if a > b:
            return 1
        else:
            return -1
    elif tong(a) > tong(b):
        return 1
    else:
        return -1

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = functools.cmp_to_key(cmp))
    for i in a:
        print(i, end=" ")
    print()
# 1
# 8
# 143 43 22 99 7 9 1111 10000000
