from math import floor, inf
from fractions import Fraction
from itertools import product

class FreeValue:
    def __init__(self, position, minimum=0, maximum=inf, multiple=1, offset=0):
        self.minimum = minimum
        self.maximum = maximum
        self.position = position
        self.multiple = multiple
        self.offset = offset

class MinimumFinder:
    def __init__(self, equations=[], free_values=[]):
        self.equations = equations
        self.free_values_values = free_values
        self.free_values = {}
        self.values = []
        for free_value in free_values:
            self.free_values[free_value] = FreeValue(free_value)

    def call(self):
        self.find_free_values_parameters()
        return self.find_minimum()

    def find_minimum(self):
        minimum = inf
        for values in product(*self.generate_values()):
            total = self.calculate_total(values)
            if total < minimum:
                minimum = total
        return minimum

    def generate_values(self):
        values = []
        for free_value in self.free_values.values():
            v = list(range(free_value.minimum, free_value.maximum + 1, free_value.multiple))
            values.append(v)
        return values

    def calculate_total(self, values):
        paired_values = list(zip(values, self.free_values.values()))
        equation_total = sum(values)
        for equation in self.equations:
            total = equation[-1] - sum([equation[p[1].position] * p[0] for p in paired_values])
            if total < 0:
                return inf
            equation_total += total
        return equation_total

    def are_equations_valid(self):
        for equation in self.equations:
            non_free_values = [value for i, value in enumerate(equation[:-1]) if value != 0 and i not in self.free_values_values]
            if len(non_free_values) > 1:
                return False
        return True

    def find_free_values_parameters(self):
        # first iteration
        for free_value in self.free_values.values():
            for equation in self.equations:
                free_value.maximum = min(free_value.maximum, self.maximum_value(equation, free_value.position))
        # # second iteration
        for free_value in self.free_values.values():
            for equation in self.equations:
                adjusted_equations = self.adjust_equation(equation, free_value.position)
                if adjusted_equations:
                    maximum = max(self.maximum_value(adjusted_equations[0], free_value.position),
                                  self.maximum_value(adjusted_equations[1], free_value.position))
                    free_value.maximum = min(free_value.maximum, maximum)

    def adjust_equation(self, equation, free_value):
        other_free_values_in_equation = [i for i, value in enumerate(equation) if i in self.free_values_values and i != free_value and value != 0]
        if len(other_free_values_in_equation) != 1:
            return False
        equation1 = [value for value in equation]
        equation2 = [value for value in equation]
        other_free_value = other_free_values_in_equation[0]
        if self.free_values[other_free_value].maximum == inf:
            return False
        equation1[-1] -= equation[other_free_value] * self.free_values[other_free_value].minimum
        equation2[-1] -= equation[other_free_value] * self.free_values[other_free_value].maximum
        equation1[other_free_value] = 0
        equation2[other_free_value] = 0
        return [equation1, equation2]

    def total_presses(self):
        counter = [0] * (len(self.equations[0]) - 1)
        print(counter)
        for equation in self.equations:
            print(equation[:-1])
            for i, value in enumerate(equation[:-1]):
                if i in self.free_values_values:
                    counter[i] += value
        for free_value in self.free_values_values:
            counter[free_value] += 1
        return counter

    def is_valid_equation(self, equation, free_value):
        return len([value for i, value in enumerate(equation[:-1]) if value != 0 and i != free_value]) <= 1

    def maximum_value(self, equation, free_value):
        if not self.is_valid_equation(equation, free_value):
            return inf
        total = equation[-1]
        free_value_factor = equation[free_value]
        if equation[free_value] == 0:
            return inf
        if free_value_factor * total < 0:
            return inf
        return int(floor(total / free_value_factor))

    def find_multiple(self, equation, free_value):
        if not self.is_valid_equation(equation, free_value):
            return [1, 0]
        total = equation[-1]
        free_value_factor = equation[free_value]
        if total.denominator > 1:
            if total.denominator != free_value_factor.denominator:
                return [1, 0]
            if (total.numerator % total.denominator) != (free_value_factor.numerator % total.denominator):
                return [1, 0]
            return [free_value_factor.denominator, (free_value_factor.numerator % total.denominator)]
        return [free_value_factor.denominator, 0]