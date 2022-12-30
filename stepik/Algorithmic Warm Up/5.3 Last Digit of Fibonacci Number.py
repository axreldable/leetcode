def fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fibonacci_last_digit(n):
    current, next = 0, 1
    for _ in range(n):
        current, next = next, (current + next) % 10

    return current


if __name__ == '__main__':
    # n = int(input())
    # print(fibonacci_last_digit(n))

    print(fibonacci_last_digit(2))
    print(fibonacci_last_digit(3))
    print(fibonacci_last_digit(5))
    print(fibonacci_last_digit(10))
    print(fibonacci_last_digit(139))
    print(fibonacci_last_digit(91239))
