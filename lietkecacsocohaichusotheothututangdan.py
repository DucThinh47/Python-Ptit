a = input()
mp = {}
a1 = []
for i in range(int(len(a) / 2)):
    tmp = int(a[0]) * 10 + int(a[1])
    if tmp in mp:
        mp[tmp] += 1
    else:
        mp[tmp] = 1
    a = a[2::]
for i in mp:
    a1.append(i)
a1.sort()
for i in a1:
    print(i, end = " ")