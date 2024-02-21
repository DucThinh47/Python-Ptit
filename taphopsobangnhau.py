n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dic1 = {}
dic2 = {}
for i in a:
    dic1[i] = 1
for i in b:
    dic2[i] = 1
if dic1 == dic2:
    print("YES")
else:
    print("NO")
# print(type(c), type(d))
# print(c)
# print(d)
# 12 18
# 1 2 3 4 5 1 2 3 5 4 1 2
# 1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5