a = [int(x) for x in input().split()]
for i in range(len(a)):
    a[i] %= 42

print(len(set(a)))