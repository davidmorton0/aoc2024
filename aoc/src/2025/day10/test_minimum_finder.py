from minimum_finder import MinimumFinder
import pytest

@pytest.fixture
def problem_1():
    return [
        [
            [1, 0, 0, 1, 0, -1, 2],
            [0, 1, 0, 0, 0, 1, 5],
            [0, 0, 1, 1, 0, -1, 1],
            [0, 0, 0, 0, 1, 1, 3]
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