n = int(input())
cau, a1, a2 = 0, [], []

for i in range(n):
    s = input().split()
    if len(a2) == 0 and len(s) == 6:
        a1.append(1)
    a2.append(s)
    if len(a2) > 1 and len(s) == 6 and len(a2[-2]) == 7:
        a1.append(1)
    if len(s) == 7:
        cau += 1
    if cau == 4:
        a1.append(2)
        cau = 0
print(len(a1))
for i in a1:
    print(i)
# 8
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay