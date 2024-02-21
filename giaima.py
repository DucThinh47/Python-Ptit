t = int(input())

def solve(s):
    for i in range(1,len(s),2):
        num = int(s[i])
        for j in range(num):
            print(s[i-1],end="")
    print()

while t>=1:
    s = input()
    solve(s)
    t-=1