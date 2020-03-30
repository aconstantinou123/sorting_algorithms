from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

selection_unsorted = [99, 77, 44, 16, 1000, 7, 4, 8, 22, 3, 16, 99, 205, 33, 1, 100, 19, 12, 55]
insertion_unsorted = [99, 77, 44, 16, 1000, 7, 4, 8, 22, 3, 16, 99, 205, 33, 1, 100, 19, 12, 55]
merge_unsorted = [99, 77, 44, 16, 1000, 7, 4, 8, 22, 3, 16, 99, 205, 33, 1, 100, 19, 12, 55]
quick_unsorted = [99, 77, 44, 16, 1000, 7, 4, 8, 22, 3, 16, 99, 205, 33, 1, 100, 19, 12, 55]

test = [10, 7, 1, 3, 5, 8, 9, 6]

print('selection sort')
selection_sort_result = selection_sort(selection_unsorted)
print(selection_sort_result, '\n')

print('insertion sort')
insertion_sort_result = insertion_sort(insertion_unsorted)
print(insertion_sort_result, '\n')

print('merge sort')
merge_sort_result = merge_sort(merge_unsorted, 0, len(merge_unsorted) - 1)
print(merge_sort_result, '\n')

print('quick sort')
quick_sort_result = quick_sort(quick_unsorted, 0, len(quick_unsorted) - 1)
print(quick_sort_result, '\n')
