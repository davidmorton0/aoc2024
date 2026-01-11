from solve import Solve

class TestSolve:
    # def test_load_input(self):
    #     solve = Solve()
    #     assert solve.load_input3('example.txt') ==  [
    #         '123 328  51 64 ',
    #         ' 45 64  387 23 ',
    #         '  6 98  215 314',
    #         '*   +   *   +  ',
    #     ]
    # 
    # # def test_process_input(self):
    # #     solve = Solve()
    # #     input = solve.load_input3('example.txt')
    # #     assert solve.process_input_3(input) ==  [
    # #         '123 328  51 64 ',
    # #         ' 45 64  387 23 ',
    # #         '  6 98  215 314',
    # #         '*   +   *   +  ',
    # #     ]
    # 
    # def test_puzzle_starts(self):
    #     solve = Solve()
    #     input = solve.load_input3('example.txt')
    #     assert solve.find_puzzle_starts(input) == [0, 4, 8, 12]
    def test_part_a_example(self):
        solve = Solve()
        assert solve.solve_a("example.txt") == 4277556
    
    def test_part_a_input_1(self):
        solve = Solve()
        assert solve.solve_a("input.txt") == 4387670995909
    
    def test_part_a_input_2(self):
        solve = Solve()
        assert solve.solve_a("input_2.txt") == 5322004718681

    def test_part_b_example(self):
        solve = Solve()
        assert solve.solve_b("example.txt") == 3263827

    def test_part_b_input_1(self):
        solve = Solve()
        assert solve.solve_b("input.txt") == 9625320374409

    def test_part_b_input_2(self):
        solve = Solve()
        assert solve.solve_b("input_2.txt") == 9876636978528
