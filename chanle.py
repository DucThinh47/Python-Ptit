def check(s):
    for i in range(1, len(s)):
        if abs(int(s[i-1]) - int(s[i])) != 2:
            return False
    return True

t = int(input())

while t >= 1:
    n = input()
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    if sum % 10 == 0 and check(n) == True:
        print("YES")
    else:
        print("NO")
    t -= 1

# 3
# 1353
# 246864
# 123435