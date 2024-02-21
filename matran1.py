n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
summ1, summ2 = 0,0
for i in range(n):
    for j in range(n):
        if i < j:
            summ1 += a[i][j]
        elif j < i:
            summ2 += a[i][j]
summ = abs(summ1 - summ2)
if summ <= k:
    print("YES")
else:
    print("NO")
print(summ)


# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5
