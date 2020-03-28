from math import floor, inf

def merge_sort(a,l, h):
    if l < h:
        m = floor((l + h) / 2)
        merge_sort(a, l, m)
        merge_sort(a, m + 1, h)
        merge(a, l, m, h)
    return a
        
def merge(a, l, m, h):
    left = a[l:m + 1]
    left.append(inf)
    right = a[m + 1:h + 1]
    right.append(inf)
    i = j = 0 
    k = l
    while k <= h:
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1