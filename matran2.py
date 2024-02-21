n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
summ1, summ2 = 0, 0
for i in range(n):
    for j in range(n):
        if i + j + 1 < n:
            summ1 += a[i][j]
        elif i + j + 1 > n:
            summ2 += a[i][j]
summ = abs(summ1 - summ2)
if summ <= k:
    print("YES")
else:
    print("NO")
print(summ)