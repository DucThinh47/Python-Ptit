n = int(input())
a = [''] * n
summ = 0
for i in range(n):
    a[i] = input()
a1, a2 = [0] * n, [0] * n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            a1[i] += 1
            a2[j] += 1
for i in range(n):
    summ += a1[i] * (a1[i] - 1) / 2
    summ += a2[i] * (a2[i] - 1) /2
print(int(summ))

# 4
# CC..
# C..C
# .CC.
# .CC.