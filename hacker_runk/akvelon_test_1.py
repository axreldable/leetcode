#!/bin/python


#
# Complete the 'getMaxArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import defaultdict

d = {}

d_calls = {
    "naive_calls": 0,
    "calls": 0
}


def mex(arr):
    s = set()
    for i in arr:
        s.add(i)
    if len(s) == 0:
        return 0
    for i in range(0, max(s) + 2):
        if i not in s:
            return i
    return 0


def is_first_greater(arr1, arr2):
    i = 0
    while True:
        if i == len(arr1) or i == len(arr2) or arr1[i] != arr2[i]:
            break
        i += 1
    if i == len(arr1):
        return False
    if i == len(arr2):
        return True
    if arr1[i] > arr2[i]:
        return True


def getMaxArray_naive(arr):
    d_calls["naive_calls"] += 1
    # print(arr)
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [mex([arr[0]])]
    else:
        rez_arrays = []
        for i in range(0, len(arr)):
            # print("rez", arr[:i + 1], arr[i + 1:])
            rez = [mex(arr[:i + 1])]

            marr = getMaxArray_naive(arr[i + 1:])
            rez += marr

            # print("rez", rez)
            rez_arrays.append(rez)
        # print("rez_arrays", rez_arrays)
        if len(rez_arrays) == 0:
            return []
        elif len(rez_arrays) == 1:
            return rez_arrays[0]
        else:
            max_i = 0
            for i in range(1, len(rez_arrays)):
                if is_first_greater(rez_arrays[i - 1], rez_arrays[max_i]):
                    max_i = i - 1
            return rez_arrays[max_i]

def getMaxArray(arr):
    d_calls["calls"] += 1
    # print(arr)
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [mex([arr[0]])]
    elif str(arr) in d:
        return d[str(arr)]
    else:
        rez_arrays = []
        for i in range(0, len(arr)):
            # print("rez", arr[:i + 1], arr[i + 1:])
            rez = [mex(arr[:i + 1])]

            marr = getMaxArray(arr[i + 1:])
            # d[len(arr[i + 1:])] = marr
            d[str(arr[i + 1:])] = marr
            rez += marr

            # print("rez", rez)
            rez_arrays.append(rez)
        # print("rez_arrays", rez_arrays)
        if len(rez_arrays) == 0:
            return []
        elif len(rez_arrays) == 1:
            return rez_arrays[0]
        else:
            max_i = 0
            for i in range(1, len(rez_arrays)):
                if is_first_greater(rez_arrays[i - 1], rez_arrays[max_i]):
                    max_i = i - 1
            return rez_arrays[max_i]


if __name__ == '__main__':
    # print(getMaxArray([1, 2, 3]))
    print(str([1]))
    print([1, 2, 3][:1])
    print([1, 2, 3][1:])
    print(getMaxArray([2, 2, 3, 4, 0, 1, 2, 0]))
    print(getMaxArray_naive([2, 2, 3, 4, 0, 1, 2, 0]))

    print("naive_calls", d_calls["naive_calls"])
    print("calls", d_calls["calls"])
