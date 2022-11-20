# python3
from os import listdir


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """

    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps
    def left_child(i):
        i += 1
        return 2 * i - 1

    def right_child(i):
        i += 1
        return 2 * i

    def shift_down(i, arr, size):
        # print(i)
        min_index = i
        l = left_child(i)
        # print(l, min_index)
        if l < size and arr[l] < arr[min_index]:
            min_index = l
        r = right_child(i)
        # print(r, min_index)
        if r < size and arr[r] < arr[min_index]:
            min_index = r
        if i != min_index:
            swaps.append((i, min_index))
            arr[i], arr[min_index] = arr[min_index], arr[i]
            shift_down(min_index, arr, size)

    size = len(data)
    swaps = []
    for i in range(size // 2, 0, -1):
        shift_down(i-1, data, size)

    # print(data)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

    # files = listdir("tests")
    # files.sort()
    # for i, file in enumerate(files):
    #     if file.endswith(".a"):
    #         with open("tests/" + files[i - 1], "r") as f:
    #             content = f.readlines()
    #             n = int(content[0])
    #             arr = list(map(int, content[1].split()))
    #             print("arr", arr)
    #         with open("tests/" + files[i], "r") as f:
    #             content = f.readlines()
    #             n_answer = int(content[0])
    #             arr_answer = list(map(lambda swap_el: swap_el.strip().split(), content[1:]))
    #
    #         arr_rez = build_heap(arr)
    #
    #         print("arr", arr)
    #         print("arr_answer", arr_answer)
    #         print("arr_rez", arr_rez)
    #
    #         print(n_answer, len(arr_rez))
    #         assert len(arr_rez) == n_answer
    #         for (i, j), (k, s) in zip(arr_answer, arr_rez):
    #             # print(i, k)
    #             assert int(i) == int(k)
    #             # print(j, s)
    #             assert int(j) == int(s)
