t = int(input())
while t >= 1:
    p,q = input().split()
    s = input().split()
    if len(s) == 1:
        s1 = s[0]
        s2 = input()
    else:
        s1 = s[0]
        s2 = s[1]
    res1 = int(s1.replace(p,q)) + int(s2.replace(p,q))
    res2 = int(s1.replace(q,p)) + int(s2.replace(q,p))
    print(min(res1, res2), max(res1, res2))
    t -= 1
