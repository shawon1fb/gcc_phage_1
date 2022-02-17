import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    # min required required bananas must eat
    min_to_eat = 1
    max_to_eat = max(piles)

    while min_to_eat < max_to_eat:
        mid = (max_to_eat + min_to_eat) // 2
        hour_spent = 0
        for p in piles:
            hour_spent += math.ceil(p / mid)

        # if this is a workable speed then search further
        if hour_spent <= h:
            max_to_eat = mid
        else:
            min_to_eat = mid + 1

    return max_to_eat


def run_this_file():
    print(min_eating_speed(piles=[3, 6, 7, 11], h=8) == 4)
    print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=5) == 30)
    print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=6) == 23)
