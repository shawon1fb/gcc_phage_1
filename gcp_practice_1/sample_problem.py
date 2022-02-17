
if __name__ == '__main__':
    t: int = int(input())
    for case in range(t):
        (bags, kids) = tuple(map(int, input().split()))
        sm: int = 0

        lst = list(map(int, input().split()))

        for i in range(bags):
            sm += lst[i]

        print(f"Case #{case+1}: {sm % kids}")
