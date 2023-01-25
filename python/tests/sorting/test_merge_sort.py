import pytest
from merge_sort.merge import merge_sort

def test_merge_sort():
  # Check if the function sorts the list correctly
  list = [38, 27, 43, 3, 9, 82, 10]
  merge_sort(list)
  assert list == [3, 9, 10, 27, 38, 43, 82]

def test_merge_sort_sorted():
  # Check if the function works with an already sorted list
  list = [1, 2, 3, 4, 5]
  merge_sort(list)
  assert list == [1, 2, 3, 4, 5]

def test_merge_sort_empty():
  # Check if the function works with an empty list
  list = []
  merge_sort(list)
  assert list == []

def test_merge_sort_reverse():
  # Check if the function works with a reverse-sorted list
  list = [20, 18, 12, 8, 5, -2]
  merge_sort(list)
  assert list == [-2, 5, 8, 12, 18, 20]

def test_merge_sort_unique():
  # Check if the function works with an list with few unique values
  list = [5, 12, 7, 5, 5, 7]
  merge_sort(list)
  assert list == [5, 5, 5, 7, 7, 12]

def test_merge_sort_nearly_sorted():
  # Check if the function works with a nearly-sorted list
  list = [2, 3, 5, 7, 13, 11]
  merge_sort(list)
  assert list == [2, 3, 5, 7, 11, 13]

def test_merge_sort_with_negative_numbers():
  list = [38, 27, -43, 3, -9, 82, 10]
  merge_sort(list)
  assert list == [-43, -9, 3, 10, 27, 38, 82]

def test_merge_sort_with_single_element():
  list = [38]
  merge_sort(list)
  assert list == [38]
