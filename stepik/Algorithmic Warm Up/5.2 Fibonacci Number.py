def fibonacci_number_naive(n):
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    if n <= 1:
        return n

    first = 0
    second = 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


if __name__ == '__main__':
    # input_n = int(input())
    # print(fibonacci_number(input_n))

    print(fibonacci_number(3))
    print(fibonacci_number(10))
