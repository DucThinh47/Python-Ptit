t = int(input())
while t >= 1:
    s = input()
    if s[0] == s[-1]:
        print("YES")
    else:
        print("NO")
    t -= 1