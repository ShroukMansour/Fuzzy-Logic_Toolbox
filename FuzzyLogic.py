class FuzzyLogic:
    def __init__(self, variables):
        self.variables = variables

    def fuzzify(self):
        for var in self.variables:
            if var != None:
                print(var.name)
                var.calc_membership()

    def infer(self, rules):
        return pred_var


    def defuzzify(self):
        return pred_value
