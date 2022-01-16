from typing import List


def isPosible(v1, v2):
    return (v1 >= 0 and v2 >= 0)


def count_negatives(grid: List[List[int]]) -> List[int]:
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

            if isPosible(r_mid - 1, c_mid - 1) and grid[r_mid - 1][c_mid - 1] >= 0:
                required_r_mid = r_mid
                required_c_mid = c_mid
                break
            r_up = r_mid - 1
            c_up = c_mid - 1
        else:
            r_low = r_mid + 1
            c_low = c_mid + 1

    return [required_r_mid, required_c_mid]






