from typing import List

"""output = 0"""
test_case_1 = [[1]]
"""output = 1"""
test_case_2 = [[-1]]
"""output = 1"""
test_case_3 = [[1, -1]]
"""output = 4"""
test_case_4 = [[-1, -1], [-1, -1]]
"""output = 2"""
test_case_5 = [[1, 1], [1, 1], [-1, -1]]


def is_possible(v1, v2):
    return v1 >= 0 and v2 >= 0


def count_negatives(grid: List[List[int]]) -> int:
    """TODO: failed approach"""
    # r_low = 0
    # r_up = len(grid) - 1
    # c_low = 0
    # c_up = len(grid[0]) - 1
    #
    # required_r_mid = -1
    # required_c_mid = -1
    #
    # while (r_low <= r_up) and (c_low <= c_up):
    #     r_mid = (r_up + r_low) // 2
    #     c_mid = (c_up + c_low) // 2
    #
    #     "if negative"
    #     if grid[r_mid][c_mid] < 0:
    #         if is_possible(r_mid - 1, c_mid - 1):
    #             if grid[r_mid - 1][c_mid - 1] >= 0:
    #                 required_r_mid = r_mid
    #                 required_c_mid = c_mid
    #                 break
    #         else:
    #             required_r_mid = r_mid
    #             required_c_mid = c_mid
    #             break
    #         r_up = r_mid - 1
    #         c_up = c_mid - 1
    #     else:
    #         r_low = r_mid + 1
    #         c_low = c_mid + 1
    #
    # count = 0
    #
    # """count all values raw wise"""
    # for i in range(len(grid) - 1, required_r_mid - 1, -1):
    #     for j in range(len(grid[0]) - 1, -1, -1):
    #         if grid[i][j] < 0:
    #             count += 1
    #
    # """count column wise"""
    # for i in range(required_r_mid - 1, -1, -1):
    #     for j in range(len(grid[0]) - 1, required_c_mid - 1, -1):
    #         if grid[i][j] < 0:
    #             count += 1
    #
    # # print(f'required row = {required_c_mid}, column = {required_r_mid}')
    #
    # return count

    """solution 1"""
    # count: int = 0
    #
    # for row in grid:
    #     for i in range(len(row) - 1, -1, -1):
    #         if row[i] >= 0:
    #             break
    #         count += 1
    #
    # return count

    """solution 2, more efficient"""
    count: int = 0
    row: int = len(grid)
    col: int = len(grid[0])

    r: int = row - 1
    c = 0

    while r >= 0 and c < col:
        if grid[r][c] < 0:
            count += (col - c)
            r -= 1
        else:
            c += 1

    return count


def run_this_file():
    print(f'test case 1 : {count_negatives(test_case_1)}')
    print(f'test case 2 : {count_negatives(test_case_2)}')
    print(f'test case 3 : {count_negatives(test_case_3)}')
    print(f'test case 4 : {count_negatives(test_case_4)}')
    print(f'test case 5 : {count_negatives(test_case_5)}')
