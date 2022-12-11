def binary_search(arr, el):
    def inner_search(arr, el, l, r):
        if l > r:
            return False

        mid = int((l + r) / 2)
        if el == arr[mid]:
            return mid
        elif el < arr[mid]:
            return inner_search(arr, el, l, mid - 1)
        else:
            return inner_search(arr, el, mid + 1, r)

    return inner_search(arr, el, 0, len(arr))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr)
    print(binary_search(arr, 2))
    arr = [2, 7, 11, 15]
    print(arr)
    print(binary_search(arr, 2))
    arr = [3, 2, 4]
    print(arr)
    print(binary_search(arr, 2))
    arr = [3, 3]
    print(arr)
    print(binary_search(arr, 2))

    # for l in (1, 5, 10, 15):
    #     for max_elem in (1, 100, 1000):
    #         arr = [randint(0, max_elem) for _ in range(l)]
    #         # print(arr)
    #         s_arr = sorted(arr)
    #         # print(s_arr)
    #         # bubble_sort(arr)
    #         # optimize_bubble_sort(arr)
    #         # selection_sort(arr)
    #         insertion_sort(arr)
    #         assert s_arr == arr
