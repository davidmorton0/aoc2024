class MinimumFinder:
    def __init__(self, equations=[], free_values=[]):
        self.equations = equations
        self.free_values = free_values

    def are_equations_valid(self):
        for equation in self.equations:
            non_free_values = [value for i, value in enumerate(equation[:-1]) if value != 0 and i not in self.free_values]
            print(equation, non_free_values)
            if len(non_free_values) > 1:
                return False
        return True

    def total_presses(self):
        counter = [0] * (len(self.equations[0]) - 1)
        print(counter)
        for equation in self.equations:
            print(equation[:-1])
            for i, value in enumerate(equation[:-1]):
                if i in self.free_values:
                    counter[i] += value
        for free_value in self.free_values:
            counter[free_value] += 1
        return counter