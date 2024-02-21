def solve(s):
    st = {-1}
    for i in s:
        st.add(i)
    for i in range(0, len(s)-2):
        if s[i] != s[i+2]:
            return False
    if len(st) != 3:
        return False
    return True

t = int(input())
while t>=1:
    s = input()
    if solve(s) == True:
        print("YES")
    else:
        print("NO")
    t-=1

# 3
# 12121212
# 343433
# 78789989
 