from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    left: int = 0
    for right in range(0, len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            k += 1 if nums[left] == 0 else 0
            left += 1

    return right - left + 1


def run_this_file():
    print(longest_ones(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6)
    print(longest_ones(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10)
