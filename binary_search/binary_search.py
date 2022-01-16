def binary_search(arr, key) -> int:
    l = 0
    u = len(arr) - 1

    while l <= u:
        m = (u + l) // 2
        # print(f"l: {l}, u: {u}, m: {m}")
        if arr[m] == key:
            return m
        elif arr[m] < key:
            l = m + 1
        else:
            u = m - 1

    return -1
