from math import floor, inf

class MinMaxFinder:
    def __init__(self, equations=[], free_values=[]):
        self.equations = equations
        self.free_values = free_values

    def call(self):
        for equation in self.equations:
            positive_free_values = []
            negative_free_values = []
            total = equation[-1]

            for free_value in self.free_values:
                if equation[free_value.position] > 0:
                    positive_free_values.append(free_value)
                elif equation[free_value.position] < 0:
                    negative_free_values.append(free_value)

            if total < 0 and len(positive_free_values) == 0 and len(negative_free_values) == 1:
                for free_value in negative_free_values:
                    free_value.minimum = max(free_value.minimum, int(floor(total / equation[free_value.position])))
            if total > 0 and len(negative_free_values) == 0:
                for free_value in positive_free_values:
                    free_value.maximum = min(free_value.maximum, int(floor(total / equation[free_value.position])))

    def calculate_from_2_free_value_equations(self):
        # do other free values in equation have a maximum
        for equation in self.equations:
            for free_value in self.free_values:
                if equation[free_value.position] > 0:
                    other_positive_free_values = [other_free_value for other_free_value in self.free_values if other_free_value != free_value and equation[other_free_value.position] > 0]
                    max_other_negative_free_values = sum([other_free_value.maximum * equation[other_free_value.position] for other_free_value in self.free_values if other_free_value != free_value and equation[other_free_value.position] < 0])
                    total = equation[-1] - max_other_negative_free_values
                    if total > 0 and max_other_negative_free_values < inf and len(other_positive_free_values) == 0:
                        free_value.maximum = min(free_value.maximum, int(floor(total / equation[free_value.position])))
        [a.print() for a in self.free_values]