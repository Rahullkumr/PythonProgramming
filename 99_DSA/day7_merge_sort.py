# merge sort
def merge(a, l, r):
    i,j,k = 0,0,0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            i, k = i+1, k+1

        else:
            a[k] = r[j]
            j, k = j+1, k+1

    while i < len(l):
        a[k] = l[i]
        i, k = i+1, k+1

    while j < len(r):
        a[k] = r[j]
        j, k = j+1, k+1

arr = [1,8,7,5,18,3,2]
# divide(arr)


# complete this