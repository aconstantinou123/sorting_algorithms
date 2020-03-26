def insertion_sort(a):
    i = 1
    while i <= len(a) - 1:
        element = a[i]
        j = i - 1
        while j >= 0 and  a[j] > element:
            a[j + 1] = a[j]
            j = j -1
        a[j + 1] = element
        i = i + 1
    return a