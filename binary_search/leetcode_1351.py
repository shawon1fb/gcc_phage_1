from typing import List


def is_possible(v1, v2):
    return v1 >= 0 and v2 >= 0


def count_negatives(grid: List[List[int]]) -> int:
    r_low = 0
    r_up = len(grid) - 1
    c_low = 0
    c_up = len(grid[0]) - 1

    required_r_mid = -1
    required_c_mid = -1

    while (r_low <= r_up) and (c_low <= c_up):
        r_mid = (r_up + r_low) // 2
        c_mid = (c_up + c_low) // 2

        "if negative"
        if grid[r_mid][c_mid] < 0:
            if is_possible(r_mid - 1, c_mid - 1):
                if grid[r_mid - 1][c_mid - 1] >= 0:
                    required_r_mid = r_mid
                    required_c_mid = c_mid
                    break
            else:
                required_r_mid = r_mid
                required_c_mid = c_mid
                break
            r_up = r_mid - 1
            c_up = c_mid - 1
        else:
            r_low = r_mid + 1
            c_low = c_mid + 1

    count = 0

    """count all values raw wise"""
    for i in range(len(grid) - 1, required_r_mid - 1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] < 0:
                print(grid[i][j])
                count += 1

    """count column wise"""
    for i in range(required_r_mid - 1, -1, -1):
        for j in range(len(grid[0]) - 1, required_c_mid-1, -1):
            if grid[i][j] < 0:
                print(grid[i][j])
                count += 1

    print(f'required row = {required_c_mid}, column = {required_r_mid}')

    return count
