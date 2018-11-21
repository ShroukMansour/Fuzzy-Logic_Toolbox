from Range import Range
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.range = Range(p1.x, p2.x)

    def get_intersection(self, val):
        m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        y = m * (val - self.p1.x) + self.p1.y
        return y



