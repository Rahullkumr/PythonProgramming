# MERGE SORT

"""
It is a type of sorting algorithm that uses the divide-and-conquer approach to sort elements by repeatedly dividing the array into smaller parts and merging them in sorted order.

steps:
Divide: Split the array into two halves recursively until each sublist contains a single element or no elements. 
Conquer: Sort each of the smaller sublists. 
Merge: Combine the sorted sublists into a single sorted array by comparing elements from each sublist. 
Recursive Process: Repeat the divide, conquer, and merge steps until the entire array is sorted.
"""

def merge_sort(arr):
    if len(arr) < 2:
        return arr 

    # breaking the array until single-single arrays
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merging single-single arrays into final sorted array
    i=j=k=0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else: 
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

arr = [9, 2, 4, 1, 0, 5]
print(merge_sort(arr))
