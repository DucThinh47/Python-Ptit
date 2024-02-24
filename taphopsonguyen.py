n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dic1, dic2 = {}, {}
for i in a:
    dic1[i] = 1
for i in b:
    dic2[i] = 1
for i in sorted(list(dic1)):
    if i in dic2:
        print(i,end=" ")
print()
for i in sorted(list(dic1)):
    if i not in dic2:
        print(i,end=" ")
print()
for i in sorted(list(dic2)):
    if i not in dic1:
        print(i,end=" ")

# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8