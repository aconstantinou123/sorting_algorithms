from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

unsorted = [99, 77, 16, 1000, 7, 4, 8, 22, 3, 99, 205, 33, 1, 100, 19, 55]

test = [1, 5, 7, 8, 2, 4, 6, 9]

print('selection sort')
selection_sort_result = selection_sort(unsorted)
print(selection_sort_result)

print('insertion sort')
insertion_sort_result = insertion_sort(unsorted)
print(insertion_sort_result)

print('merge sort')
merge_sort_result = merge_sort(unsorted, 0, len(unsorted) - 1)
print(merge_sort_result)
