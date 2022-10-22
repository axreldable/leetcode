#!/bin/python


#
# Complete the 'getMaxArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

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
    if len(arr1) > len(arr2):
        i = 0
        while True:
            if arr1[i] != arr2[i]:
                break
            i += 1
            if i >= len(arr2):
                break
        if i == len(arr2):
            return True
        if arr1[i] > arr2[i]:
            return True
        else:
            return False
    elif len(arr1) < len(arr2):
        i = 0
        while True:
            if arr1[i] != arr2[i]:
                break
            i += 1
            if i >= len(arr1):
                break
        if i == len(arr1):
            return False
        if arr1[i] > arr2[i]:
            return True
        else:
            return False
    else:
        i = 0
        while True:
            if arr1[i] != arr2[i]:
                break
            i += 1
            if i >= len(arr1):
                break
        if i == len(arr1):
            return False
        if arr1[i] > arr2[i]:
            return True
        else:
            return False


def getMaxArray(arr):
    # print(arr)
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [mex([arr[0]])]
    else:
        rez_arrays = []
        for i in range(0, len(arr)):
            rez = [mex(arr[:i + 1])]
            rez += getMaxArray(arr[i + 1:])
            # print("rez", rez)
            print("rez", arr[:i + 1], arr[i + 1:])
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
    print(getMaxArray([2, 2, 3, 4, 0, 1, 2, 0]))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # arr_count = int(raw_input().strip())
    #
    # arr = []
    #
    # for _ in xrange(arr_count):
    #     arr_item = int(raw_input().strip())
    #     arr.append(arr_item)
    #
    # result = getMaxArray(arr)
    #
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
