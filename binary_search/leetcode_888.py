from typing import List


def fair_candy_swap(alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
    alice_sum = sum(alice_sizes)
    bob_sum = sum(bob_sizes)

    gor = abs(alice_sum - bob_sum) // 2
    for a in alice_sizes:
        if (a + gor) in bob_sizes:
            return [a, a + gor]
    return []


def run_this_file():
    print(fair_candy_swap(alice_sizes=[1, 1], bob_sizes=[2, 2]) == [1, 2])
    print(fair_candy_swap(alice_sizes=[1, 2], bob_sizes=[2, 3]) == [1, 2])
    print(fair_candy_swap(alice_sizes=[2], bob_sizes=[1, 3]) == [2, 3])
    print(fair_candy_swap(alice_sizes=[1, 2, 5], bob_sizes=[2, 4]) == [5, 4])
