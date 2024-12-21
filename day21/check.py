import functools
import itertools


def day21(s, *, part2=True):
    yx_of_digit = dict(
        [('7', (0, 0)), ('8', (0, 1)), ('9', (0, 2)), ('4', (1, 0)), ('5', (1, 1)), ('6', (1, 2))]
        + [('1', (2, 0)), ('2', (2, 1)), ('3', (2, 2)), ('0', (3, 1)), ('A', (3, 2))]
    )
    yx_of_dir = dict([('^', (0, 1)), ('A', (0, 2)), ('<', (1, 0)), ('v', (1, 1)), ('>', (1, 2))])

    # Length of the shortest final sequence to move from (y, x) to (y2, x2) on the digit keypad
    # given that the previous direction code (from the last directional keypad) was `last_dir_ch`.
    def digit_cost(y, x, y2, x2, last_dir_ch='A'):
        if (y, x) == (y2, x2):
            return dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir['A'])
        min_cost = 10 ** 18
        if y != y2 and not (x == 0 and y2 == 3):  # Move up or down.
            y1, ch = (y + 1, 'v') if y2 > y else (y - 1, '^')
            cost1 = dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir[ch])
            min_cost = min(min_cost, cost1 + digit_cost(y1, x, y2, x2, ch))
        if x != x2 and not (y == 3 and x2 == 0):  # Move left or right.
            x1, ch = (x + 1, '>') if x2 > x else (x - 1, '<')
            cost1 = dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir[ch])
            min_cost = min(min_cost, cost1 + digit_cost(y, x1, y2, x2, ch))
        return min_cost

    # Length of the shortest final sequence to move from (y, x) to (y2, x2) on the n_dir'th
    # directional keypad given that the previous direction code (from the prior directional keypad
    # n_dir - 1, if n_dir > 0) was `last_dir_ch`.
    @functools.cache
    def dir_cost(y, x, y2, x2, n_dir=3 if part2 else 2, last_dir_ch='A'):
        if n_dir == 0:
            return 1  # On the zero'th directional keypad, all codes cost exactly 1.
        if (y, x) == (y2, x2):
            return dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir['A'], n_dir - 1)  # Move to 'A'.
        min_cost = 10 ** 18
        if y != y2 and not (x == 0 and y2 == 0):  # Move up or down.
            y1, ch = (y + 1, 'v') if y2 > y else (y - 1, '^')
            cost1 = dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir[ch], n_dir - 1)
            min_cost = min(min_cost, cost1 + dir_cost(y1, x, y2, x2, n_dir, ch))
        if x != x2 and not (y == 0 and x2 == 0):  # Move left or right.
            x1, ch = (x + 1, '>') if x2 > x else (x - 1, '<')
            cost1 = dir_cost(*yx_of_dir[last_dir_ch], *yx_of_dir[ch], n_dir - 1)
            min_cost = min(min_cost, cost1 + dir_cost(y, x1, y2, x2, n_dir, ch))
        return min_cost

    def code_cost(code):
        yxs = [yx_of_digit[ch] for ch in 'A' + code]
        return sum(digit_cost(*yx, *yx2) for yx, yx2 in itertools.pairwise(yxs))

    [print(code_cost(code)) for code in s.splitlines()]

    return sum(code_cost(code) * int(code.rstrip('A')) for code in s.splitlines())

with open('input_h.txt', 'r') as s:
    print(day21(s.read()))