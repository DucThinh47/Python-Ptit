def giaiThua(n):
    res = 1
    for i in range(n):
        res *= i + 1
    return res

def check(n):
    res = 0
    tmp = n
    while n > 0:
        res += giaiThua(n % 10)
        n = int(n / 10)
    if res == tmp:
        return "Yes"
    else:
        return "No"
t = int(input())
while t > 0:
    n = int(input())
    print(check(n))
    t -= 1