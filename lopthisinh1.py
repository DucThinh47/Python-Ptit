class ThiSinh:
    def __init__(self, name, dob, diem1, diem2, diem3):
        self.name = name
        self.dob = dob
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong_diem = diem1 + diem2 + diem3
    def out(self):
        print(self.name, self.dob, "{:.1f}".format(self.tong_diem))

name = input()
dob = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
t = ThiSinh(name, dob, diem1, diem2, diem3)
t.out()

# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5