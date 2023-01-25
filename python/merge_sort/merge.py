def merge_sort(list):
    n = len(list)

    if n > 1:
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        print(f"left before sort: {left} and right before sort: {right}")
        merge_sort(left)
        merge_sort(right)
        print(f"left after sort: {left} and right after sort: {right}")

        print(f"left before merge: {left} and right before merge: {right}")
        print(f"list before merge: {list}")
        merge(left, right, list)
        print(f"left after merge: {left} and right after merge: {right}")
        print(f"list after merge: {list}")

def merge(left, right, list):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

# Usage example
list = [8,4,23,42,16,15]
# print(f"before merge sort: {list}")
merge_sort(list)
# print(f"after merge sort: {list}")
