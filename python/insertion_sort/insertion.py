import pytest
#python/tests/sorting/test_insertion_sort.py

def insertion_sort(arr):
    for i in range(1, len(arr)):
        print("before while:", arr)
        j = i-1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            # print(arr)
        arr[j + 1] = temp
        print("after while:", arr)
    return

# insertion_sort([20, 18, 12, 8, 5, -2])
