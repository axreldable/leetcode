from random import randint


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


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


def fibonacci_sum_squares(n):
    rez = fibonacci_huge(n, 10) * fibonacci_huge(n + 1, 10)
    return rez % 10


def stress_test(n):
    count = 0
    while True:
        count += 1
        n = randint(1, n)
        rez_1 = fibonacci_sum_squares_naive(n)
        rez_2 = fibonacci_sum_squares(n)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == '__main__':
    # input = sys.stdin.read()
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))

    print(fibonacci_sum_squares(7))  # 3
    print(fibonacci_sum_squares(73))  # 1
    print(fibonacci_sum_squares(1234567890))  # 0

    # stress_test(100)
