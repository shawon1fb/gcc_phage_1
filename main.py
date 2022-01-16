from binary_search.binary_search import binary_search
from binary_search.leetcode_1351 import count_negatives


def main():
    # lst = [
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, -1],
    #     [1, 1, 1, 1, -1, -1, -1],
    #     [1, 1, 1, 1, -1, -1, -1],
    # ]

    lst = [[1,-1]]

    l = count_negatives(lst)
    #print(l)


if __name__ == '__main__':
    main()
