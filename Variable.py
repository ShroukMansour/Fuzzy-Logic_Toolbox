class Variable:

    def __init__(self, name, value, sets):
        self.name = name
        self.value = value
        self.sets = dict(((x.name, x) for x in sets))

    def calc_membership(self):
        for set in self.sets.values():
            if set != None:
                if set.check_range(self.value, set.range):
                    set.membership = set.calc_membership(self.value)
                else:
                    set.membership = 0
                print(self.value, ", " , set.name, set.membership)

