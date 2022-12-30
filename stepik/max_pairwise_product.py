from random import randint


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product(numbers):
    first = -1
    second = -1

    for el in numbers:
        if el > first:
            second = first
            first = el
        elif el > second:
            second = el

    return first * second


def stress_test(n, m):
    count = 0
    while True:
        count += 1
        arr = [randint(0, m) for _ in range(randint(2, n))]
        print(arr)
        rez_1 = max_pairwise_product_naive(arr)
        rez_2 = max_pairwise_product(arr)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    # print(max_pairwise_product(input_numbers))

    stress_test(10, 100_000)
    # stress_test(5, 10)

    assert max_pairwise_product([100_000, 90_000]) == 9_000_000_000
    assert max_pairwise_product(list(i for i in range(1, 2 * 10 ** 5 + 1))) == 39_999_800_000
