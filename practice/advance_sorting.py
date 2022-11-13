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
            k += 1
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


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 2, 3, 4, 5, 122, 46, 78, 4, 29]
    print(arr)
    merge_sort(arr)
    print(arr)

    for l in (1, 5, 10, 15):
        for max_elem in (1, 100, 1000):
            arr = [randint(0, max_elem) for _ in range(l)]
            # print(arr)
            s_arr = sorted(arr)
            merge_sort(arr)
            assert s_arr == arr
