from random import randint


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp


def optimize_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
        if is_sorted:
            break


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_i = i
        for j in range(i, n):
            if arr[j] < arr[max_i]:
                max_i = j
        tmp = arr[i]
        arr[i] = arr[max_i]
        arr[max_i] = tmp


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr_elem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= curr_elem:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_elem


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 2, 3, 4, 5, 122, 46, 78, 4, 29]
    print(arr)
    # bubble_sort(arr)
    # optimize_bubble_sort(arr)
    # selection_sort(arr)
    insertion_sort(arr)
    print(arr)

    for l in (1, 5, 10, 15):
        for max_elem in (1, 100, 1000):
            arr = [randint(0, max_elem) for _ in range(l)]
            # print(arr)
            s_arr = sorted(arr)
            # print(s_arr)
            # bubble_sort(arr)
            # optimize_bubble_sort(arr)
            # selection_sort(arr)
            insertion_sort(arr)
            assert s_arr == arr
