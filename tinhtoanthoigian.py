class Gamer:
    thoi_gian = 0
    def __init__(self, ma, ten, gio_vao, gio_ra):
        self.ma = ma
        self.ten = ten
        self.thoi_gian = gio_ra[0] * 60 + gio_ra[1] - gio_vao[0] * 60 - gio_vao[1]

    def out(self):
        print(self.ma, self.ten, int(self.thoi_gian / 60), "gio", self.thoi_gian % 60, "phut")

n = int(input())
a = []
for i in range(n):
    ma = input()
    ten = input()
    gio_vao = [int(x) for x in input().split(':')]
    gio_ra = [int(x) for x in input().split(':')]
    a.append(Gamer(ma,ten,gio_vao,gio_ra))

a = sorted(a, key = lambda x : (-x.thoi_gian))
for i in a:
    i.out()


# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00