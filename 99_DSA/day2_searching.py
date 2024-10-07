# algorithm
# flowchart

# searching:
#     1. linear
#     2. binary

'''
1. Linear Search algorithm
    It is a searching algorithm which works on a principle called SEQUENTIAL SEARCHing, where control will
    traverse through each and every value present in a collection one after the other sequentially to check whether
    key is present or not.

Steps to follow for Linear search:
    s1: consider a list collection and key to check
    s2: start comparing the values from 0th index till length-1 of the collection
    s3: after getting the value same as key, return its index.
    s4: if key is not present, then ignore

Note:
    In Linear search algo, if value is not present then also control will compare the values by performing N-iterations.
    To overcome this problem, we use Binary Search algorithm

2. Binary Search algorithm
    - It is a searching algorithm which works on sorted collection
    - using BSA, it is possible to increase efficiency by reducing the no of comparisons
Steps:
    s1: consider a list collection and key to check
    s2: initialize the least index as 0 and highest index as len(arr)-1
    s3: check whether least index <= highest index
    s4: calculate mid-index using
            mid = (least i+ei)//2
    s5: check whether key == collection[mid-index],
        if true, return the mid-index
        elif check key > collection[mid]
            if true, change least-index = mid-index + 1
        else check key < collection[mid]
            if true, change highest-index = mid-index - 1
    s6: repeat all step from s3 to s5, until you get index of key
'''

# Linear Search
print('---------------Linear Search---------------')
def linear_search(list, key):
    for i in range(len(list)):
        if key == list[i]:
            print(i)
linear_search([11, 12, 13, 14, 15], 13)
linear_search((161, 162, 163, 164, 165), 165)
linear_search(['apple', 'ball', 'cat', 'dog', 'god'], 'god')


# Binary Search
print('---------------Binary Search---------------')
def binary_search(list, key):
    start_index = 0
    end_index = len(list) - 1
    while start_index <= end_index:
        mid_index = start_index + end_index // 2
        if key == list[mid_index]:
            return mid_index
        elif key > list[mid_index]:
            start_index = mid_index + 1
        elif key < list[mid_index]:
            end_index = mid_index - 1

print(binary_search([11, 12, 13, 14, 15], 13))
linear_search((161, 162, 163, 164, 165), 165)
linear_search(['apple', 'ball', 'cat', 'dog', 'god'], 'god')