a = [i.lower() for i in input().split(" ")]
b = [i.lower() for i in input().split(" ")]
dic1, dic2, dic3 = {}, {}, {}
for i in a:
    dic1[i] = 1
    dic2[i] = 1
for i in b:
    dic1[i] = 1
    dic3[i] = 1
dic1 = sorted(list(dic1))
for i in dic1:
    print(i, end=" ")
print()
dic2 = sorted(list(dic2))
for i in dic2:
    if i in dic3:
        print(i, end=" ")

# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++