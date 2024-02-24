n = int(input())
a = [int(x) for x in input().split()]
s = 10**9
for i in a:
    x = 0
    #i = 13
    for j in a:
        #j = 34
        x += abs(i - j)
        #x = x + (13 - 13) = 38 + (13 - 34) = 59
        # print(x, end=" ")
    if s > x:
        #s = 59
        #p = 13
        s = x
        p = i
print(s, p)
# 8
# 13 5 8 7 9 15 26 34