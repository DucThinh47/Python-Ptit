s = input()
cnt_hoa = 0
cnt_thuong = 0
for i in s:
    if i.islower():
        cnt_thuong += 1
    else:
        cnt_hoa += 1
if cnt_thuong >= cnt_hoa:
    print(s.lower())
else:
    print(s.upper())