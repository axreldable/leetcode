def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def pisano_period(m):
    if m <= 1:
        return

    first = 0
    second = 1
    p = 0
    while True:
        p += 1
        # print(first, second)
        first, second = second, (first + second) % m
        if first == 0 and second == 1:
            return p


def fibonacci_huge(n, m):
    period = pisano_period(m)
    n = n % period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # print(fibonacci_huge_naive(n, m))

    print(pisano_period(1))

    print(fibonacci_huge(1, 239))
    print(fibonacci_huge(115, 1000))
    print(fibonacci_huge(2816213588, 239))
