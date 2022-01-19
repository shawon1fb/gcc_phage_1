from typing import List


def target_indices(nums: List[int], target: int) -> List[int]:
    """TODO: Tow pointer approach"""
    nums = sorted(nums)
    left: int = 0
    right: int = len(nums) - 1
    found_at: int = -1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            found_at = mid
            break
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if found_at < 0:
        return []

    left = found_at - 1
    right = found_at
    res: List[int] = []

    while left >= 0 and nums[left] == target:
        res.append(left)
        left -= 1

    while right < len(nums) and nums[right] == target:
        res.append(right)
        right += 1

    return sorted(res)


def run_this_file():
    print(target_indices(nums=[1, 2, 5, 2, 3], target=2) == [1,2])
    """ Output = [1,2] """
    print(target_indices(nums=[1, 2, 5, 2, 3], target=3) == [3])
    """ Output: [3] """
    print(target_indices(nums=[1, 2, 5, 2, 3], target=5) == [4])
    """ Output: [4] """
