t = int(input())
while t >= 1:
    n = input()
    res = 10 ** 5
    tmp = 0
    for i in range(int(len(n))):
        if n[i].isalpha():
            if i != 0 and n[i-1].isdigit():
                res = min(res, tmp)
                tmp = 0
        else:
            tmp = tmp * 10 + int(n[i])
    print(res)
    t -= 1