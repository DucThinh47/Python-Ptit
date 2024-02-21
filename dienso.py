t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    cnt = 0
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    minn = min(a)
    maxx = max(a)
    for i in range(minn, maxx + 1):
        if i not in dic:
            cnt += 1
    print(cnt)

# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3