import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutGon(self):
        uc = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / uc)
        self.mau = int(self.mau / uc)
    def out(self):
        print(self.tu, "/", self.mau, sep="")

tu, mau = [int(x) for x in input().split()]
ps = PhanSo(tu,mau)
ps.rutGon()
ps.out()

