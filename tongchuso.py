def solve(s):
    summ = 0
    for i in s:
        summ += ord(i) - ord('0')
        #s = 919 summ = 9 + 1 + 9
    return str(summ)

s = input()
cnt = 0
while len(s) > 1:
    s = solve(s)
    cnt += 1
print(cnt)