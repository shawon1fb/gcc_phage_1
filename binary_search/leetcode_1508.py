"""Problem not solved I literally stuck with this problem"""

from typing import List


def range_sum(nums: List[int], n: int, left: int, right: int) -> int:
    sum_of_subs: List[int] = []

    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]
        sum_of_subs.append(summ)

    return sum(sum_of_subs[left - 1:right]) % 1000000007


def run_this_file():
    print(range_sum(nums=[1, 2, 3, 4], n=4, left=1, right=5) == 13)
    print(range_sum(nums=[1, 2, 3, 4], n=4, left=3, right=4) == 6)
    print(range_sum(nums=[1, 2, 3, 4], n=4, left=1, right=10) == 50)
