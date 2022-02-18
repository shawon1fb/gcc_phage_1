vls: set = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}


def main():
    t: int = int(input())
    for i in range(t):
        k_name = input()
        last = k_name[len(k_name) - 1]
        roller = 'Bob'
        if last in vls:
            roller = 'Alice'
        elif last == 'y' or last == 'Y':
            roller = 'nobody'
        print(f'Case #{i + 1}: {k_name} is ruled by {roller}.')


if __name__ == '__main__':
    main()
