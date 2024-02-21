def check(a):
    if min(a) == max(a):
        return True
    return False

while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        k = int(input())
        a.append(k)
    if check(a) == True:
        print("BANG NHAU")
    else:
        print(min(a), max(a))