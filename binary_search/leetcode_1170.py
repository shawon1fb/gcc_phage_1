from typing import List


def get_count(s: str) -> int:
    dic = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }
    small = s[0]
    memo = dict()
    for c in s:
        if c in memo:
            memo[c] = memo[c] + 1
        else:
            memo[c] = 1
        # update the smallest value
        if dic[small] >= dic[c]:
            small = c
    return memo[small]


def get_large_count(lst: List[int], k: int) -> int:
    ln: int = len(lst) - 1
    count: int = 0
    while ln >= 0 and lst[ln] > k:
        count += 1
        ln -= 1
    return count


def num_smaller_by_frequency(queries: List[str], words: List[str]) -> List[int]:
    ws: List[int] = []
    for s in words:
        ws.append(get_count(s))
    ws = sorted(ws)

    res: List[int] = []

    for s in queries:
        q_count: int = get_count(s)
        res.append(get_large_count(ws, q_count))

    return res


def run_this_file():
    print(num_smaller_by_frequency(queries=["cbd"], words=["zaaaz"]) == [1])
    print(num_smaller_by_frequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]) == [1, 2])
