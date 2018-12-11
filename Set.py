import numpy as np
from Range import Range
from Line import Line


class Set:
    def __init__(self, name, points):
        self.name = name
        self.points = np.array(points)
        self.membership = -1
        self.range = self.calc_range()
        self.centroid = self.calc_centroid()
        self.lines = self.calc_lines()

    def calc_membership(self, val):
        memship = -1
        for line in self.lines:
            if self.check_range(val, line.range):
                memship = line.get_intersection(val)
                break
        return memship

    def calc_range(self):
        return Range(self.points[0].x, self.points[self.points.shape[0] - 1].x)

    def check_range(self, val, range):
        if (val >= range.strt and val <= range.end):
            return True
        else:
            return False

    def calc_centroid(self):
        a = 0
        cx = 0
        for i in range(0, self.points.size - 1):
            a = a + (self.points[i].x * self.points[i + 1].y - self.points[i + 1].x * self.points[i].y)
            cx = cx + ((self.points[i].x + self.points[i + 1].x) * (
                        self.points[i].x * self.points[i + 1].y - self.points[i + 1].x * self.points[i].y))
        a = 0.5 * a
        return cx / (6 * a)

    def calc_lines(self):
        lines = np.empty([3, ], dtype=object)
        bool_strt = True
        bool_end = True
        for i in range(self.points.shape[0] - 1):
            if self.points[0].x == self.points[1].x and self.points[self.points.shape[0] - 1].x == self.points[
                self.points.shape[0] - 2].x:
                lines[0] = Line(self.points[1], self.points[2])
                break
            elif self.points[0].x == self.points[1].x and bool_strt:
                lines[0] = Line(self.points[1], self.points[2])
                bool_strt = False
            elif self.points[self.points.shape[0] - 1].x == self.points[self.points.shape[0] - 2].x and bool_end:
                lines[0] = Line(self.points[0], self.points[1])
                bool_end = False
            else:
                lines[i] = Line(self.points[i], self.points[i + 1])
        return lines
