# 2. selection sort

'''
selection sort is a sorting algorithm, where the element present inside the collection will get
sorted by considering its minimum position

in this swapping of values takes place only once in a complete pass

# steps:
    1. consider a list collection to be sorted
    2. initialise a variable with assumed minimum position
    3. compare the values with assumed min position if it is greater 
    change the min position value
    4. at last swap value present at actual min position with assumed minimum position
    5. repeat the steps from 2 to 4 till length of the collection
'''

import random as r
randon_list = []
for x in range(1,6):
    randon_list.append(r.randint(1,100))
print('random list: ', randon_list)


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


#
min = 0
for i in range(len(randon_list)):
    for j in range(i+1, len(randon_list)):
        if randon_list[min] > randon_list[j]:
            min = j
    randon_list[min], randon_list[j]
    print(randon_list)


















