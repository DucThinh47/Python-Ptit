import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x0 = self.x - other.x
        y0 = self.y - other.y
        return math.sqrt(x0 * x0 + y0 * y0)

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def solve(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if (max(a,b,c) * 2 >= a + b + c):
            print("INVALID")
        else:
            print("{:.3f}".format(a + b + c))

t = int(input())
while t > 0:
    a = []
    a += [float(x) for x in input().split()]
    i = 0
    triangle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triangle.solve()
    i += 6
    t -= 1

# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0
