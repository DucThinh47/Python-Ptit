class NhanVien:
    def __init__(self,ma, ten, lt, th):
        self.ma = "TS0" + str(ma)
        self.ten = ten
        self.lt = lt
        self.th = th
        if lt > 10:
            lt /= 10
        if th > 10:
            th /= 10
        self.tb = (lt + th) / 2
        if self.tb < 5:
            self.loai = "TRUOT"
        elif self.tb >= 5 and self.tb < 8:
            self.loai = "CAN NHAC"
        elif self.tb >= 8 and self.tb <= 9.5:
            self.loai = "DAT"
        else:
            self.loai = "XUAT SAC"

n = int(input())
a = []
for i in range(n):
    ten = input()
    lt = float(input())
    th = float(input())
    a.append(NhanVien(i+1, ten, lt, th))
a.sort(key = lambda x : x.tb, reverse=True)
for i in a:
    print(i.ma, i.ten, "{:.2f}".format(i.tb), i.loai)

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56

