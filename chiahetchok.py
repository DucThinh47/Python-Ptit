a,k,n = [int(x) for x in input().split()]
b = k - a % k + a
ok = 0
for i in range(b, n + 1, k):
    ok = 1
    print(i - a, end = " ")
if ok == 0:
    print("-1")
#a = 10, k = 6, n = 40
#b = 6 - 10 % 6 + 10 = 6 - 4 + 10 = 12
#for i in range(12, 41, 6)
#12 - 10 = 2
#18 - 10 = 8


