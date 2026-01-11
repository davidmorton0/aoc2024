from minimum_finder import MinimumFinder, FreeValue
import pytest
from math import inf
from fractions import Fraction

@pytest.fixture
def problem_1():
    return [
        [
            [1, 0, 0, 1, 0, -1, 2], # 5=0, 3 max 2. 5=3, 3 max 5.
            [0, 1, 0, 0, 0, 1, 5], # 5 max 5
            [0, 0, 1, 1, 0, -1, 1], # 5=0, 3 max 1, 5=3, 3 max 4.
            [0, 0, 0, 0, 1, 1, 3] # 5 max 3
        ],
            [3, 5]
    ]

@pytest.fixture
def problem_2():
    return [
        [
            [1, 0, 1, 0, 0, 2],
            [0, 1, -1, 0, 0, 5],
            [0, 0, 0, 1, 0, 5],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ],
            [2]
    ]

@pytest.fixture
def problem_3():
    return [
        [
            [1, 0, 0, 1, 6],
            [0, 1, 0, -1, -1],
            [0, 0, 1, 0, 5],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
            [3]
    ]

@pytest.fixture
def problem_65():
    return [
        [
            [1, 0, 0, 0, 0, 0, 0, 4, 3, 87], # 7 max 21, 8 max 29
            [0, 1, 0, 0, 0, 0, 0, -3, -1, 52], # any value
            [0, 0, 1, 0, 0, 0, 0, -2, -1, -26], # any value
            [0, 0, 0, 1, 0, 0, 0, 3, 3, 74], # 7 max 24, 8 max 24
            [0, 0, 0, 0, 1, 0, 0, -2, -2, -31], # any value
            [0, 0, 0, 0, 0, 1, 0, 0, -1, 9], # any value
            [0, 0, 0, 0, 0, 0, 1, -1, -1, -19] # any value
        ],
            [7, 8]
    ]

@pytest.fixture
def problem_28():
    return [
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 17],
            [0, 1, 0, 0, 0, 0, 0, -2, -28],
            [0, 0, 1, 0, 0, 0, 0, 1, 39],
            [0, 0, 0, 1, 0, 0, 0, 1, 20],
            [0, 0, 0, 0, 1, 0, 0, 0, 19],
            [0, 0, 0, 0, 0, 1, 0, -1, -3],
            [0, 0, 0, 0, 0, 0, 1, 0, 19],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
            [7]
    ]

@pytest.fixture
def minimum_finder():
    return MinimumFinder()

@pytest.mark.parametrize("fixture", ["problem_1", "problem_2"])
def test_are_valid_equations_valid(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    assert minimum_finder.are_equations_valid() is True

def test_are_invalid_equations_invalid(minimum_finder):
    minimum_finder.equations = [[1, 1, 1, 5]]
    minimum_finder.free_values = [1]

    assert minimum_finder.are_equations_valid() is False

@pytest.mark.parametrize("fixture,result",
                         [
                            ("problem_1", [0, 0, 0, 3, 0, 1]),
                            ("problem_2", [0, 0, 1, 0, 0])
                         ])
def test_total_presses(fixture, result, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    assert minimum_finder.total_presses() == result

# def test_min_max_values(minimum_finder):
#     minimum_finder.free_values_values = [3]
#     # has maximum
#     assert minimum_finder.min_max_values([1, 0, 0, 1, 2], 3) == [inf, 2]
#     # no maximum
#     assert minimum_finder.min_max_values([1, 0, 0, 1, -2], 3) == [inf, inf]
#     # no maximum
#     assert minimum_finder.min_max_values([1, 0, 0, -1, 2], 3) == [inf, inf]
#     # both negative, so maximum
#     assert minimum_finder.min_max_values([1, 0, 0, -1, -2], 3) == [2, inf]
#     # 2 free values, still maximum
#     assert minimum_finder.min_max_values([1, 0, 1, 1, 2], 3) == [inf, 2]
#     # other non-free value
#     assert minimum_finder.min_max_values([0, 0, 1, 1, 2], 3) == [inf, 2]
#     # free value multiplied by 2
#     assert minimum_finder.min_max_values([1, 0, 0, 2, 2], 3) == [inf, 1]
#     assert minimum_finder.min_max_values([1, 0, 0, 2, 4], 3) == [inf, 2]
#     # free value multiplied by 2 and round
#     assert minimum_finder.min_max_values([1, 0, 0, 2, 3], 3) == [inf, 1]
#     # free value multiplier is fraction
#     assert minimum_finder.min_max_values([1, 0, 0, Fraction(1, 2), 2], 3) == [inf, 4]
#     # total and multiplier are fractions
#     assert minimum_finder.min_max_values([1, 0, 0, Fraction(1, 2), Fraction(1, 2)], 3) == [inf, 1]
#     # total and multiplier are larger fractions
#     assert minimum_finder.min_max_values([1, 0, 0, Fraction(1, 2), Fraction(7, 2)], 3) == [inf, 7]

def test_find_multiple(minimum_finder):
    # fractional free value multiplier
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(1, 2), 2], 3) == [2, 0]
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(1, 2), 3], 3) == [2, 0]
    # fractional totals
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(1, 2), Fraction(1, 2)], 3) == [2, 1]
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(3, 2), Fraction(3, 2)], 3) == [2, 1]
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(3, 4), Fraction(3, 4)], 3) == [4, 3]
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(3, 2), Fraction(1, 2)], 3) == [2, 1]
    # invalid equation
    assert minimum_finder.find_multiple([1, 1, 0, 1, 2], 3) == [1, 0]
    # different denominators
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(1, 2), Fraction(1, 3)], 3) == [1, 0]
    # different numerators
    assert minimum_finder.find_multiple([1, 0, 0, Fraction(2, 3), Fraction(1, 3)], 3) == [1, 0]

@pytest.mark.parametrize("fixture", ["problem_1"])
def test_find_free_values_parameters1(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.find_free_values_parameters()
    free_value_1 = minimum_finder.free_values[3]
    free_value_2 = minimum_finder.free_values[5]
    free_value_1.print()
    free_value_2.print()
    assert free_value_1.position == 3
    assert free_value_1.maximum == 4
    assert free_value_1.minimum == 0
    assert free_value_1.multiple == 1
    assert free_value_1.offset == 0
    assert free_value_2.position == 5
    assert free_value_2.maximum == 3
    assert free_value_2.minimum == 0
    assert free_value_2.multiple == 1
    assert free_value_2.offset == 0

@pytest.mark.parametrize("fixture", ["problem_2"])
def test_find_free_values_parameters2(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.find_free_values_parameters()
    free_value_1 = minimum_finder.free_values[2]
    assert free_value_1.position == 2
    assert free_value_1.maximum == 2
    assert free_value_1.minimum == 0
    assert free_value_1.multiple == 1
    assert free_value_1.offset == 0

@pytest.mark.parametrize("fixture", ["problem_65"])
def test_find_free_values_parameters65(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.find_free_values_parameters()
    free_value_1 = minimum_finder.free_values[7]
    free_value_2 = minimum_finder.free_values[8]
    assert free_value_1.maximum == 21
    assert free_value_2.maximum == 24

@pytest.mark.parametrize("fixture", ["problem_28"])
def test_find_free_values_parameters28(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.find_free_values_parameters()
    free_value_1 = minimum_finder.free_values[7]
    assert free_value_1.maximum == 20


@pytest.mark.parametrize("fixture", ["problem_1"])
def test_adjust_equation(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.free_values[5].maximum = 3
    assert minimum_finder.adjust_equation([1, 0, 0, 1, 0, -1, 2], 3) == [
        [1, 0, 0, 1, 0, 0, 2],
        [1, 0, 0, 1, 0, 0, 5]
    ]

@pytest.mark.parametrize("fixture", ["problem_1"])
def test_non_adjusted_equation(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.free_values[5].maximum = 3
    equation = [1, 0, 0, 0, 0, -1, 2]
    assert minimum_finder.adjust_equation(equation, 5) is False

def test_generate_values_1_free(minimum_finder):
    minimum_finder.free_values = {
        1: FreeValue(position=1,minimum=0,maximum=1,multiple=1),
    }
    assert minimum_finder.generate_values() == [[0], [1]]

def test_generate_values_2_free(minimum_finder):
    minimum_finder.free_values = {
        1: FreeValue(position=1,minimum=0,maximum=1,multiple=1),
        2: FreeValue(position=2, minimum=2, maximum=5, multiple=2),
    }
    assert minimum_finder.generate_values() == [(0, 2), (0, 4), (1, 2), (1, 4)]

@pytest.mark.parametrize("fixture,result", [("problem_1", 10), ("problem_2", 12), ("problem_3", 11)])
def test_find_minimum(fixture, result, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    minimum_finder.find_free_values_parameters()
    assert minimum_finder.find_minimum() == result

@pytest.mark.parametrize("fixture", ["problem_1"])
def test_calculate_total(fixture, request):
    minimum_finder = MinimumFinder(*request.getfixturevalue(fixture))
    assert minimum_finder.calculate_total((3, 2)) == 10