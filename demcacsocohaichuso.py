a = input()
mp = {}
for i in range(int(len(a)/2)):
    tmp = int(a[0]) * 10 + int(a[1])
    if tmp in mp:
        mp[tmp] += 1
    else:
        mp[tmp] = 1
    a = a[2::]
for i in mp:
    print(i, mp[i])