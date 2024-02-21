t = int(input())
while t > 0:
    s = input()
    summ = 0
    tmp = ""
    for i in s:
        if i.isdigit():
            summ += int(i)
        else:
            tmp += i
    print("".join(sorted(tmp)), summ, sep="")
    t -= 1
#join: join element in tuple
#ex: mytuple = ("thinh", "ok")
#".".join(mytuple) = thinh.ok

# 2
# AC2BEW3
# ACCBA10D2EW30