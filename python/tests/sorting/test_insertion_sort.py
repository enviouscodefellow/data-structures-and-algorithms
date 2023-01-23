import pytest
from insertion_sort.insertion import insertion_sort

# @pytest.mark.skip("TODO")
def test_empty_list():
    # test on an empty list
    arr = []
    insertion_sort(arr)
    assert arr == []

# @pytest.mark.skip("TODO")
def test_sorted_list():
    # test on a sorted list
    arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

# @pytest.mark.skip("TODO")
def test_unsorted_list():
    # test on an unsorted list
    arr = [3, 2, 4, 1, 5]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

# @pytest.mark.skip("TODO")
def test_negative_numbers():
    # test on a list with negative numbers
    arr = [-1, 3, -4, 2, -5]
    insertion_sort(arr)
    assert arr == [-5, -4, -1, 2, 3]

# @pytest.mark.skip("TODO")
def test_reverse_sorted():
   # test on a reverse-sorted list
    arr = [20, 18, 12, 8, 5, -2]
    insertion_sort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

# @pytest.mark.skip("TODO")
def test_few_unique_elements():
    # test on a list with few unique elements
    arr = [5, 12, 7, 5, 5, 7]
    insertion_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

# @pytest.mark.skip("TODO")
def test_nearly_sorted():
    # test on a nearly-sorted list
    arr = [2, 3, 5, 7, 13, 11]
    insertion_sort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]
