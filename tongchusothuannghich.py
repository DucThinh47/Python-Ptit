def checktn(s):
    tmp = s[::-1]
    if tmp == s and len(s) > 1:
        return "YES"
    else:
        return "NO"

t = int(input())
while t>=1:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    tmp = str(sum)
    print(checktn(tmp))
    t -= 1

# 2
# 12341
# 22222222222222222222