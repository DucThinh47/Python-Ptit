import math


class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def rutGon(self):
        uc = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / uc)
        self.mau = int(self.mau / uc)
    def cong(self, other):
        tu1 = self.tu * other.mau + self.mau * other.tu
        mau1 = self.mau * other.mau
        self.tu = tu1
        self.mau = mau1
    def out(self):
        print(self.tu, "/", self.mau, sep="")

line = [int(x) for x in input().split()]
ps1 = PhanSo(line[0], line[1])
ps2 = PhanSo(line[2], line[3])
ps1.cong(ps2)
ps1.rutGon()
ps1.out()