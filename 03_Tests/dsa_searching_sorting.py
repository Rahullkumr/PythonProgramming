# Basic Binary Search
# Question:
# Implement the binary search algorithm to find the index of a target element in a sorted array.
# Example:
# •	Input: arr = [1, 3, 5, 7, 9, 11], target = 7
# •	Output: 3 (index of 7)
'''
def binary_search(arr, target):
    si, ei = 0, len(arr) - 1
    while si <= ei:
        mid = (si + ei)//2
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            si = mid + 1
        if target < arr[mid]:
            ei = mid - 1
arr, target = [1, 3, 5, 7, 9, 11], 7
print(binary_search(arr, target))
'''



# Binary Search for the Last Occurrence
# Question:
# Modify the binary search to return the index of the last occurrence of the target in the sorted array.
# Example:
# •	Input: arr = [1, 3, 3, 3, 5, 7, 9], target = 3
# •	Output: 3 (index of the last occurrence of 3)
'''
def bin_search_4lastOccurence(arr, target):
    si, ei = 0, len(arr) - 1
    while si <= ei:
        mid = (si + ei)//2
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            si = mid + 1
        if target < arr[mid]:
            ei = mid - 1
arr, target = [1, 3, 3, 3, 5, 7, 9], 3
print(bin_search_4lastOccurence(arr[::-1], target))
'''



# Basic Linear Search
# Question:
# Implement a basic linear search algorithm to find the index of a target element in an unsorted array.
# Example:
# •	Input: arr = [10, 15, 20, 25], target = 20
# •	Output: 2 (since 20 is at index 2)
'''
def linear_search(arr, target):
    for i in arr:
        if target == i:
            return arr.index(i)
arr, target = [10, 15, 20, 25], 20
print(linear_search(arr, target))
'''



# Linear Search - Find Maximum Element
# Question:
# Write a linear search algorithm to find the maximum element in an unsorted list.
# Example:
# •	Input: arr = [4, 8, 2, 9, 5]
# •	Output: 9 (since 9 is the largest element)
'''
def linear_search(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max
arr = [4, 8, 2, 9, 5]
print(linear_search(arr))
'''



# Basic Bubble Sort Implementation
# Question:
# Implement the bubble sort algorithm to sort an array in ascending order.
# Example:
# •	Input: arr = [5, 2, 9, 1, 5, 6]
# •	Output: [1, 2, 5, 5, 6, 9]
'''
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr 

arr = [5, 2, 9, 1, 5, 6]
print(bubble_sort(arr))
'''



# Bubble Sort - Sort in Descending Order
# Question:
# Modify the bubble sort algorithm to sort the array in descending order.
# Example:
# •	Input: arr = [5, 2, 9, 1, 5, 6]
# •	Output: [9, 6, 5, 5, 2, 1]
"""
def bubble_sort_desc(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr
arr = [5, 2, 9, 1, 5, 6]
print(bubble_sort_desc(arr))
"""



# Basic Selection Sort
# Question:
# Implement the basic selection sort algorithm to sort an array in ascending order.
# Example:
# •	Input: arr = [64, 25, 12, 22, 11]
# •	Output: [11, 12, 22, 25, 64]
'''
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
'''



# Selection Sort - Sort in Descending Order
# Question:
# Modify the selection sort algorithm to sort an array in descending order.
# Example:
# •	Input: arr = [64, 25, 12, 22, 11]
# •	Output: [64, 25, 22, 12, 11]
'''
def selection_sort_desc(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort_desc(arr))
'''



# Basic Insertion Sort
# Question:
# Implement the basic insertion sort algorithm to sort an array in ascending order.
# Example:
# •	Input: arr = [12, 11, 13, 5, 6]
# •	Output: [5, 6, 11, 12, 13]
'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j != 0:
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr 
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
'''



# Insertion Sort - Sort in Descending Order
# Question:
# Modify the insertion sort algorithm to sort an array in descending order.
# Example:
# •	Input: arr = [12, 11, 13, 5, 6]
# •	Output: [13, 12, 11, 6, 5]
'''
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        j = i
        while j != 0:
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr 
arr = [12, 11, 13, 5, 6]
print(insertion_sort_desc(arr))
'''



# Basic Quick Sort
# Question:
# Implement the basic quick sort algorithm to sort an array in ascending order.
# Example:
# •	Input: arr = [10, 7, 8, 9, 1, 5]
# •	Output: [1, 5, 7, 8, 9, 10]
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))
'''





# Quick Sort - Sort in Descending Order
# Question:
# Modify the quick sort algorithm to sort an array in descending order.
# Example:
# •	Input: arr = [10, 7, 8, 9, 1, 5]
# •	Output: [10, 9, 8, 7, 5, 1]

def quick_sort_desc(myarr):
    if len(myarr) <= 1:
        return myarr
    else:
        pivot = myarr[0]
        lesser = [x for x in myarr[1:] if x >= pivot]
        greater = [x for x in myarr[1:] if x < pivot]
        return quick_sort_desc(lesser) + [pivot] + quick_sort_desc(greater)


arr = [10, 7, 8]
print(arr)
print(quick_sort_desc(arr))

