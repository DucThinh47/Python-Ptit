t = int(input())
while t > 0:
    n = int(input())
    m = {}
    maxx = 0
    tmp = 0
    a = input().split()
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    for i in a:
        if m[i] > maxx:
            maxx = m[i]
            tmp = i
    if maxx > n / 2:
        print(tmp)
    else:
        print("NO")
    t -= 1