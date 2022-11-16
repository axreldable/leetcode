from random import randint


def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def quick_sort(arr, l, r):
    def partition(arr, l, r):
        pivot = arr[r]

        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]

        return i + 1

    if l >= r:
        return

    p_index = partition(arr, l, r)
    quick_sort(arr, l, p_index - 1)
    quick_sort(arr, p_index + 1, r)


def optimized_quick_sort(arr, l, r):
    def partition(arr, l, r):
        pivot = arr[r]

        i = k = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                k += 1
                arr[k], arr[j] = arr[j], arr[k]
                arr[k], arr[i] = arr[i], arr[k]
            elif arr[j] == pivot:
                k += 1
                arr[k], arr[j] = arr[j], arr[k]
        arr[k + 1], arr[r] = arr[r], arr[k + 1]

        return i + 1, k + 1

    if l >= r:
        return

    k = randint(l, r)
    arr[l], arr[k] = arr[k], arr[l]

    ll, rr = partition(arr, l, r)
    quick_sort(arr, l, ll - 1)
    quick_sort(arr, rr + 1, r)


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 2, 3, 4, 5, 122, 46, 78, 4, 29]
    print(arr)
    # merge_sort(arr)
    # quick_sort(arr, 0, len(arr) - 1)
    optimized_quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    for l in (1, 5, 10, 15):
        for max_elem in (1, 100, 1000):
            arr = [randint(0, max_elem) for _ in range(l)]
            # print(arr)
            s_arr = sorted(arr)
            # merge_sort(arr)
            # quick_sort(arr, 0, len(arr) - 1)
            optimized_quick_sort(arr, 0, len(arr) - 1)
            assert s_arr == arr
