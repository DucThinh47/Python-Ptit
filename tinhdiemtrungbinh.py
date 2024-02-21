n = int(input())
a = [float(x) for x in input().split()]
maxx = max(a)
minn = min(a)
summ = 0
cnt_maxx = 0
cnt_minn = 0
for i in a:
    summ += i
    if i == maxx:
        cnt_maxx += 1
    if i == minn:
        cnt_minn += 1
print("{:.2f}".format((summ - cnt_maxx * maxx - cnt_minn * minn) / (n - cnt_maxx - cnt_minn)))

# 6
# 6.75 8 9.2 7.25 7.75 6.75
