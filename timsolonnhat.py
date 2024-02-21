t = int(input())
while t >= 1:
    n = input()
    n = n + "z"
    res = -1
    tmp = 0
    for i in range(len(n)):
        if n[i].isalpha():
            if i != 0 and n[i-1].isdigit():
                res = max(res, tmp)
                tmp = 0
        else:
            tmp = tmp * 10 + int(n[i])
    print(res)
    t -= 1