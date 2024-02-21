t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    tmp = []
    for i in range(n):
        while len(tmp) > 0 and a[tmp[-1]] <= a[i]:
            tmp.pop()
        if len(tmp) == 0:
            print(i+1, end=" ")
        else:
            print(i-tmp[-1],end=" ")
        tmp.append(i)
    print()
# 1
# 7
# 100 80 60 70 60 75 85