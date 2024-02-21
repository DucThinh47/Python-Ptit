def mucGia(ten,ghe):
    if ten == "Xe_con":
        if ghe == "5":
            return 10000
        else:
            return 15000
    if ten == "Xe_tai":
        return 20000
    if ten == "Xe_khach":
        if ghe == "29":
            return 50000
        else:
            return 70000
n = int(input())
dic = {}
for i in range(n):
    a = input().split()
    if a[3] == "IN":
        if a[4] not in dic:
            dic[a[4]] = mucGia(a[1],a[2])
        else:
            dic[a[4]] += mucGia(a[1],a[2])
dic = sorted(dic.items(), key=lambda x:x[0])
for i in dic:
    print(str(i[0]) + ":", i[1])

# 5
# 30F-123.15 Xe_con 5 OUT 06/11/202
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021