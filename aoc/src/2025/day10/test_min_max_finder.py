from minimum_finder import FreeValue
from min_max_finder import MinMaxFinder
import pytest
from math import inf
from fractions import Fraction

@pytest.mark.parametrize(
    "equations,free_values,min,max",
    [
        ([[1, 0, 0, 1, 2]], [FreeValue(position=3)], 0, 2),
        ([[1, 0, 0, 1, -2]], [FreeValue(position=3)], 0, inf),
        ([[1, 0, 0, -1, 2]], [FreeValue(position=3)], 0, inf),
        ([[1, 0, 0, -1, -2]], [FreeValue(position=3)], 2, inf),
        ([[1, 0, 1, 1, 2]], [FreeValue(position=2), FreeValue(position=3)], 0, 2),
        ([[0, 0, 1, 1, 2]], [FreeValue(position=3)], 0, 2),
        ([[1, 0, 0, 2, 2]], [FreeValue(position=3)], 0, 1),
        ([[1, 0, 0, 2, 4]], [FreeValue(position=3)], 0, 2),
        ([[1, 0, 0, 2, 3]], [FreeValue(position=3)], 0, 1),
        ([[1, 0, 0, Fraction(1, 2), 2]], [FreeValue(position=3)], 0, 4),
        ([[1, 0, 0, Fraction(1, 2), Fraction(1, 2)]], [FreeValue(position=3)], 0, 1),
        ([[1, 0, 0, Fraction(1, 2), Fraction(7, 2)]], [FreeValue(position=3)], 0, 7),
    ],
)
def test_min_max_values(equations,free_values,min,max):
    min_max_finder = MinMaxFinder(equations, free_values)
    min_max_finder.call()
    assert free_values[0].minimum == min
    assert free_values[0].maximum == max

def test_calculate_from_2_free_value_equations():
    equations = [[1, 0, 0, 1, 0, -1, 2]]
    free_value1 = FreeValue(position=3)
    free_value2 = FreeValue(position=5, maximum=3)
    free_values = [free_value1, free_value2]
    min_max_finder = MinMaxFinder(equations, free_values)
    min_max_finder.calculate_from_2_free_value_equations()
    assert free_value1.maximum == 5
