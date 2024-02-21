t = int(input())
while t > 0:
    s = input()
    tong = 0
    tich = 1
    mark = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                mark = 1
                tich *= int(s[i])
        else:
            tong += int(s[i])
    if mark == 0:
        tich = 0
    print(tich, tong)
    t -= 1

# 3
# 12345678
# 20000
# 22334455667788