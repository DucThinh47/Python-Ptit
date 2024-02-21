a,b = [1] * 10001, []
for i in range(2,10001):
    if a[i] == 1:
        for j in range(i * i, 10001, i):
            a[j] = 0
        b.append(i)
n = int(input())
cnt = 0
c = [int(x) for x in input().split()]
for i in c:
    s = 10**9
    for j in b:
        s = min(s, abs(i - j))
    cnt = max(cnt,s)
print(cnt)

# 8
# 13 5 8 7 9 15 26 34