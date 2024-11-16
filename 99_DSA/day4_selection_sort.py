# 2. selection sort

'''
selection sort is a sorting algorithm, where the element present inside the collection will get
sorted by considering its minimum position

in this swapping of values takes place only once in a complete pass

# steps:
    1. consider a list collection to be sorted
    2. initialise a variable with assumed minimum position
    3. compare the values with assumed min position if it is greater change the min position value
    4. at last swap value present at actual min position with assumed minimum position
    5. repeat the steps from 2 to 4 till length of the collection
'''

import random as r
randon_list = [r.randint(1, 100) for no in range(1, 6)]

# def selection_sort(list):
#     min = 0
#     for i in range(1, len(list)):
#         if list[min] > list[i]:
#             min = i
#     list[min], list[0] = list[0], list[min]
#     # list[min], list[0] = list[0], list[min]
#     print(list)
#
# selection_sort(randon_list)


# ======================= my way ======================================
'''
    sabse chota element hai usko find krna hai, then swap kro ith position se
'''


print(randon_list)
for i in range(len(randon_list)):
    min_index = i
    for j in range(i+1, len(randon_list)):
        if randon_list[j] < randon_list[min_index]:
            min_index = j
    randon_list[i], randon_list[min_index] = randon_list[min_index], randon_list[i]
print(randon_list)












