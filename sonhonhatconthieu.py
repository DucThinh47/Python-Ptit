n = int(input())
a = [int(x) for x in input().split()]

for i in range(1, 30001):
    if i not in a:
        print(i)
        break