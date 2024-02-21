t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    a = [int(x) for x in input().split()]
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if int(dic[i]) % 2 != 0:
            print(i)
            break

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2

