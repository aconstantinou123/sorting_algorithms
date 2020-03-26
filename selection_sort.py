def selection_sort(a):
    i = 0
    while i <= len(a) - 1:
        min = i
        j = i + 1
        while j < len(a):
            if a[j] < a[min]:
                min = j
            j = j + 1
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
        i = i + 1
    return a