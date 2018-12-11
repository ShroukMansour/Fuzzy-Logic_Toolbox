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

def infix_to_postfix(expression):
    p = []
    stack = []

    for term in expression:
        if isinstance(term, float) or isinstance(term, int):
            p.append(term)
        elif term == "OR":
            while len(stack) != 0 and stack[len(stack) - 1] == "AND":
                p.append(stack.pop())
            stack.append(term)
        else:
            stack.append(term)

    while len(stack) != 0:
        p.append(stack.pop())

    return p

def eval_postfix(postfix):
    stack = []

    for term in postfix:
        if isinstance(term, float) or isinstance(term, int):
            stack.append(term)
        else:
            A = stack.pop()
            B = stack.pop()
            if term == "AND":
                res = min(A,B)
            else:
                res = max(A,B)
            stack.append(res)
    return stack.pop()

def eval_expression(expression):
    postfix = infix_to_postfix(expression)
    return eval_postfix(postfix)

def process_rule(rule_info, variables):
    expression = []
    i = 1
    while i < len(rule_info)-3:
        if rule_info[i] == "AND" or rule_info[i] == "OR":
            expression.append(rule_info[i])
            i = i+1
        else:
            expression.append(variables[rule_info[i]].sets[rule_info[i+2]].membership)
            i = i+3
    output_set = rule_info[len(rule_info)-1]
    return expression, output_set


num_var = int(input('input\n'))
variables = dict()
output_variable = None
# variables data
for i in range(num_var+1):
    if i == (num_var + 1):
        print("Predicted var info: ")
    var_info = np.array(input().split(' '))
    var_name = var_info[0]
    if i != num_var:
        var_val = var_info[1]
    else:
        var_val = 0
    num_sets = int(input())
    sets = np.empty([num_sets], dtype=object)
    for j in range(num_sets):
        set_info = np.array(input().split(' '))
        set_name = set_info[0]
        set_type = set_info[1]
        points = handle_points(np.array([float(x) for x in input().split(' ')]))
        sets[j] = Set(set_name, points)
    if i != num_var:
        variables[var_name] = Variable(var_name, float(var_val), sets)
    else:
        output_variable = Variable(var_name, float(var_val), sets)

print("---------FUZZIFY--------")
fuzzy = FuzzyLogic(variables.values())
fuzzy.fuzzify()

# rules data
num_rules = int(input())

print("---------INFERENCE--------")
output_sets = np.zeros(0, dtype=object)
nom = 0
den = 0
for i in range(num_rules):
    rule_info = np.array(input().split(' '))
    rule, output_set_name = process_rule(rule_info, variables)
    membership = eval_expression(rule)
    centroid = output_variable.sets[output_set_name].centroid
    nom = nom + centroid*membership
    print(centroid)
    den = den + membership
    print(output_set_name + ": " + str(membership))

print("---------DEFUZZIFICATION--------")
print("output: ", str(nom/den))

# fuzzy.infer()
# fuzzy.defuzzify()