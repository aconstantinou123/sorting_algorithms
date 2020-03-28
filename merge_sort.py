from math import floor, inf

def merge_sort(a, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
    return a
        
def merge(a, p, q, r):
    L = a[p:q + 1]
    L.append(inf)
    R = a[q + 1:r + 1]
    R.append(inf)
    i = j = 0 
    k = p
    while k < r + 1:
        if L[i] < R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
        k = k + 1