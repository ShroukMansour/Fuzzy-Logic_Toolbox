from Variable import Variable
from Set import Set
from FuzzyLogic import FuzzyLogic
from Point import Point
import numpy as np


"""
Test cases:
3
var1 2.5
2
Left trapezoidal
0 1 3 4
Right trapezoidal
2 3 6 6
var2 5
3
A triangle
0 3 3
B trapezoidal
2.5 3 4 6
C triangle
4.5 6 8
var3 6
2
A trapezoidal
2 2 4 4
B triangle
4 4 8
outputVar
3
X trapezoidal
1 1 4 5
Y trapezoidal
4 5 7 8
Z triangle
7 8 9
4
2 var1 = Left AND var2 = A outputVar = X
2 var2 = B OR var3 = A outputVar = Y
2 var1 = Right AND var2 = C outputVar = Z
2 var3 = B AND var2 = B outputVar = X

------------
2
op 30
3
left t
0 0 50
m m
0 50 100
large k
50 100 100
pdp 80
3
left t
0 0 50
m m
0 50 100
large k
50 100 100

-----------------

2
op 50
3
left1 t
0 0 30 50
medium m
30 50 70
largge k
30 40 80 100
pdp 80
3
left2 t
0 0 50
m m
0 50 100
large k
50 100 100

"""


def handle_points(p):
    points = np.empty(p.shape[0], dtype=object)
    points[0] = Point(p[0], 0)
    for i in range(1, p.shape[0]-1):
        points[i] = Point(p[i], 1)
    points[p.shape[0] - 1] = Point(p[p.shape[0] - 1], 0)
    return points


num_var = int(input('input\n'))
variables = np.empty([num_var + 1], dtype=object)

# variables data
for i in range(num_var + 1):
    if i == (num_var + 1):
        print("Predicted var info: ")
    var_info = np.array(input().split(' '))
    var_name = var_info[0]
    var_val = var_info[1]
    num_sets = int(input())
    sets = np.empty([num_sets], dtype=object)
    for j in range(num_sets):
        set_info = np.array(input().split(' '))
        set_name = set_info[0]
        set_type = set_info[1]
        points = handle_points(np.array([float(x) for x in input().split(' ')]))
        sets[j] = Set(set_name, points)

    variables[i] = Variable(var_name, float(var_val), sets)


# rules data

num_rules = input("Rules:")

fuzzy = FuzzyLogic(variables)
fuzzy.fuzzify()
# fuzzy.infer()
# fuzzy.defuzzify()