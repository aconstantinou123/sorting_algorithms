def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    return a

def partition(a, p, r):
    x = a[r]
    i = p - 1
    j = p
    while j <= r -1:
        if a[j] <= x:
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j = j + 1
    temp = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp
    return i + 1
