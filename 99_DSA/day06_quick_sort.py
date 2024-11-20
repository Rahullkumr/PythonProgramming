# QUICK SORT

"""
- It is a type of sorting algorithm where a pivot element will be considered to store it at the sorted position
- use QUICK SORT for every coding rounds

steps:
    Choose a Pivot:
        Select an element from the array to act as the "pivot" (first, last or random element).
    Partitioning:
        Rearrange the array into two sublists:
            Lesser: Elements smaller than or equal to the pivot.
            Greater: Elements larger than the pivot.
    Recursive Sorting:
        Apply the quick sort algorithm recursively to the lesser and greater sublists.
    Combine:
        Concatenate the sorted lesser list, the pivot, and the sorted greater list to form the final sorted array.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


myarr = [5, 2, 6, 2, 7, 8, 1]
print(myarr)
print(quick_sort(myarr))
