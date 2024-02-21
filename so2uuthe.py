def check(s):
    cnt = 0
    for i in s:
        if i == '2':
            cnt += 1
    if cnt > len(s) / 2:
        return True
    return False

a, b = [], ["0", "1", "2"]

def sinh(s):
    if check(s):
        a.append(s)
    if len(s) < 10:
        for i in b:
            sinh(s + i)

sinh('1')
sinh('2')
a = sorted([int(x) for x in a])
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        print(a[j], end=" ")
    print()
