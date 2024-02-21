s = input()
tmp = ""
cnt = -2
for i in range(len(s)):
    tmp = s[-i - 1] + tmp
    if cnt % 3 == 0:
        tmp = "," + tmp
    cnt += 1
print(tmp.strip(','))

